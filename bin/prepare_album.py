"""Create browser-readable JPEG copies of album HEIC uploads before Jekyll runs."""

from pathlib import Path
import shutil
import subprocess


def prepare(album_root=Path("assets/album")):
    sources = sorted(path for path in album_root.rglob("*") if path.is_file() and path.suffix.lower() in {".heic", ".heif"})
    if not sources:
        return
    converter = shutil.which("magick") or shutil.which("convert")
    if not converter:
        raise RuntimeError("ImageMagick is required to prepare HEIC album photos.")
    for source in sources:
        destination = source.with_suffix(".jpg")
        if destination.exists():
            print(f"Using existing JPEG: {destination}")
            continue
        subprocess.run([converter, f"{source}[0]", "-auto-orient", "-strip", "-quality", "90", str(destination)], check=True)
        if not destination.read_bytes().startswith(b"\xff\xd8\xff"):
            raise RuntimeError(f"HEIC conversion did not create a JPEG: {source}")
        print(f"Prepared album photo: {source} -> {destination}")


if __name__ == "__main__":
    prepare()
