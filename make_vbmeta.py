#!/usr/bin/env python3
"""
Build a vbmeta image per AOSP libavb/avb_vbmeta_image.h.
256-byte AvbVBMetaImageHeader (big-endian) zero-padded to 4096 bytes.
flags=2 -> AVB_VBMETA_IMAGE_FLAGS_VERIFICATION_DISABLED.
"""
import struct

AVB_MAGIC = b"AVB0"
AVB_RELEASE_STRING_SIZE = 47
HEADER_SIZE = 256
IMAGE_SIZE = 4096
RELEASE_STRING = b"avbtool 1.2.0"

header = struct.pack(
    ">4sLLQQLQQQQQQQQQQQLL",
    AVB_MAGIC,                # magic
    1,                        # required_libavb_version_major
    0,                        # required_libavb_version_minor
    0,                        # authentication_data_block_size
    0,                        # auxiliary_data_block_size
    0,                        # algorithm_type (NONE)
    0, 0,                     # hash_offset, hash_size
    0, 0,                     # signature_offset, signature_size
    0, 0,                     # public_key_offset, public_key_size
    0, 0,                     # public_key_metadata_offset, _size
    0, 0,                     # descriptors_offset, descriptors_size
    0,                        # rollback_index
    2,                        # flags (VERIFICATION_DISABLED)
    0,                        # rollback_index_location
)

release = RELEASE_STRING.ljust(AVB_RELEASE_STRING_SIZE + 1, b"\x00")
reserved = b"\x00" * 80
header_block = header + release + reserved
assert len(header_block) == HEADER_SIZE, len(header_block)

image = header_block + b"\x00" * (IMAGE_SIZE - HEADER_SIZE)
assert len(image) == IMAGE_SIZE, len(image)

with open("vbmeta_disabled.img", "wb") as f:
    f.write(image)

print(f"Wrote vbmeta_disabled.img ({len(image)} bytes)")
print("First 4 bytes:", " ".join(f"{b:02x}" for b in image[:4]))
print("Flags @120:", " ".join(f"{b:02x}" for b in image[120:124]))
print("Release @128:", image[128:128+14])
