import python_nbt.nbt as nbt
from argparse import ArgumentParser
from pyvox.parser import VoxParser
from pyvox.models import Vox
import yaml


def init_parser() -> ArgumentParser:

    parser = ArgumentParser(description='Converts .vox file to minecraft .schematic files')
    parser.add_argument('filename', help='File name of input vox file')
    parser.add_argument('-o', '--output', help='Filename of output schematic file')
    parser.add_argument('-c', '--config', help='Block id list')
    return parser


def convert_vox(vox: Vox, vox_palletes: list[str], schematic_palettes: dict[str, int]) -> list[int]:

    length, width, height = vox.models[0].size
    blocks = [0] * width * length * height

    for x, y, z, c in vox.models[0].voxels:
        block_pallete_index = schematic_palettes[vox_palletes[c]]
        blocks[y + x * width + z * width * length] = block_pallete_index

    return blocks


def write_schematic(filename: str, config_filename: str, output_filename: str):

    vox = VoxParser(args.filename).parse()

    length, width, height = vox.models[0].size

    schematic_palettes, vox_pallettes = load_pallete(config_filename)
    schematic = init_schematic(width, length, height, schematic_palettes)

    blocks = convert_vox(vox, vox_pallettes, schematic_palettes)
    schematic.value['BlockData'] = nbt.NBTTagByteArray(blocks)

    if output_filename is not None:
        nbt.write_to_nbt_file(output_filename, schematic)
    else:
        nbt.write_to_nbt_file('output.schematic', schematic)


def load_pallete(pallete_file: str | None) -> tuple[dict[str, int], list[str]]:

    palette_data = {}

    if pallete_file is not None:
        with open(pallete_file, 'r') as f:
            pallete_file = yaml.safe_load(f)
            palette_data = pallete_file["palletes"]

    vox_pallettes = generate_vox_palettes(palette_data)
    schematic_palettes = generate_schematic_palettes(palette_data)

    return schematic_palettes, vox_pallettes


def generate_schematic_palettes(palette_data: dict[str, list[int]]) -> dict[str, int]:

    schematic_palette = {'minecraft:air': 0, 'minecraft:stone': 1}

    [schematic_palette.setdefault(k, len(schematic_palette)) for k in palette_data]

    return schematic_palette


def generate_vox_palettes(palette_data: dict[str, list[int]]) -> list[str]:

    vox_pallettes = ['minecraft:stone'] * 256
    vox_pallettes[0] = 'minecraft:air'

    for block_id, pallete_indices in palette_data.items():
        for pallete_index in pallete_indices:
            vox_pallettes[pallete_index] = block_id

    return vox_pallettes


def init_schematic(width: int, length: int, height: int, schematic_palette: dict) -> nbt.NBTTagCompound:

    schematic_base = nbt.NBTTagCompound()
    schematic_base.value['Palette'] = nbt.NBTTagCompound()

    for block, index in schematic_palette.items():
        schematic_base.value['Palette'].value[block] = nbt.NBTTagInt(index)
    schematic_base.value['PaletteMax'] = nbt.NBTTagInt(len(schematic_palette))

    schematic_base.value['Width'] = nbt.NBTTagShort(width)
    schematic_base.value['Length'] = nbt.NBTTagShort(length)
    schematic_base.value['Height'] = nbt.NBTTagShort(height)

    schematic_base.value['DataVersion'] = nbt.NBTTagInt(1976)
    schematic_base.value['Version'] = nbt.NBTTagInt(2)

    schematic_base.value['BlockData'] = nbt.NBTTagByteArray([0] * width * length * height)

    return schematic_base


if __name__ == "__main__":

    parser = init_parser()
    args = parser.parse_args()

    write_schematic(args.filename, args.config, args.output)
