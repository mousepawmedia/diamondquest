from diamondquest.model.map import direction
from diamondquest.model.map import blocks


def test_add_daisy_above():
    block = blocks.Block(type=blocks.BlockType.GRASS)
    block.add_decor(blocks.Decoration.DAISY, offset=direction.Direction.ABOVE)
    assert block.decor == blocks.Decoration.DAISY
    assert block.decor_offset == direction.Direction.ABOVE


def test_remove_stone():
    block = blocks.Block(type=blocks.BlockType.STONE)
    block = block.get_removed()
    assert block.type == blocks.BlockType.AIR
    assert block.variant == blocks.BlockType.STONE


def test_remove_treasure():
    block = blocks.Block(type=blocks.BlockType.TREASURE)
    block = block.get_removed()
    assert block.type == blocks.BlockType.AIR
    assert block.variant == blocks.BlockType.TREASURE


def test_remove_grass():
    block = blocks.Block(type=blocks.BlockType.GRASS)
    block = block.get_removed()
    assert block.type == blocks.BlockType.AIR
    assert block.variant == blocks.BlockType.GRASS


def test_remove_dirt():
    block = blocks.Block(type=blocks.BlockType.DIRT)
    block = block.get_removed()
    assert block.type == blocks.BlockType.AIR
    assert block.variant == blocks.BlockType.DIRT


def test_remove_air():
    block = blocks.Block(type=blocks.BlockType.AIR)
    block = block.get_removed()
    assert block.type == blocks.BlockType.AIR


def test_remove_mantle():
    block = blocks.Block(
        type=blocks.BlockType.MANTLE, variant=blocks.MantleVariant.UPPER
    )
    block = block.get_removed()
    assert block.type == blocks.BlockType.MANTLE
    assert block.variant == blocks.MantleVariant.UPPER
