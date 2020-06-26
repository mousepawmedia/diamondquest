import pygame

from diamondquest.common.constants import TEXTURE_RES
from diamondquest.common import Color, Resolution
from diamondquest.common import loader
from diamondquest.model.map import (
    BlockType,
    TreasureVariant,
    MantleVariant,
    Decoration,
)
from diamondquest.view.window import Window


class BlockTexture:
    """Stores the top-left corner for each texture in blockset.gif.
    Numbers are (X,Y) pairs.
    Numbers are offsets *in blocks* from the top-left corner of the image.
    Block size is defined separately, and must be used with these values.
    """

    texture_locations = {
        (BlockType.STONE, 0): (0, 4),
        (BlockType.MANTLE, MantleVariant.UPPER): (0, 5),
        (BlockType.MANTLE, MantleVariant.MID): (0, 6),
        (BlockType.MANTLE, MantleVariant.LOWER): (0, 7),
        (BlockType.GRASS, 0): (6, 0),
        (BlockType.DIRT, 0): (6, 1),
        (BlockType.AIR, BlockType.GRASS): (5, 0),
        (BlockType.AIR, BlockType.DIRT): (6, 2),
        (BlockType.AIR, BlockType.STONE): (6, 3),
        (BlockType.AIR, BlockType.TREASURE): (6, 4),
        (BlockType.TREASURE, TreasureVariant.FOSSIL): (7, 2),
        (BlockType.TREASURE, TreasureVariant.ARTIFACT): (7, 3),
        (BlockType.TREASURE, TreasureVariant.MINERAL): (7, 4),
        (Decoration.SPROUT, 0): (0, 0),
        (Decoration.DAISY, 0): (1, 0),
        (Decoration.DANDELION, 0): (2, 0),
    }

    cache = dict()

    @classmethod
    def texture_location(cls, block, variant=0):
        x, y = cls.texture_locations[(block, variant)]
        x *= TEXTURE_RES
        y *= TEXTURE_RES
        return (x, y, TEXTURE_RES, TEXTURE_RES)

    @classmethod
    def load_texture(cls, block, variant=0):
        """Load a surface containing the texture for a block, scaled to window.
        block - the BlockType or Decoration
        variant - the optional variant of the BlockType, default 0
        """
        try:
            return cls.cache[(block, variant)]
        except KeyError:
            blockset = loader.load_texture("blockset")

            texture = pygame.Surface(
                (TEXTURE_RES, TEXTURE_RES), pygame.SRCALPHA
            )
            if block == BlockType.AIR and variant == BlockType.AIR:
                texture.fill(Color.SKY)
            else:
                texture.blit(
                    blockset,
                    (0, 0),
                    BlockTexture.texture_location(block, variant),
                )

            bh = Resolution.get_primary().block_height
            texture = pygame.transform.scale(texture, (bh, bh))

            cls.cache[(block, variant)] = texture
            return texture
