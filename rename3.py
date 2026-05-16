import argparse
from pathlib import Path


def rename_files(folder, prefix, ext, dry_run):
    folder_path = Path(folder)

    # 檢查資料夾是否存在
    if not folder_path.exists():
        print(f"錯誤：資料夾 {folder} 不存在")
        return

    # 取得所有檔案
    files = list(folder_path.iterdir())

    # 副檔名過濾（可選）
    if ext:
        files = [f for f in files if f.suffix == ext]

    # 沒有檔案
    if not files:
        print("找不到符合條件的檔案")
        return

    # 開始改名
    for i, file in enumerate(sorted(files), start=1):
        new_name = f"{prefix}{i:03d}{file.suffix}"
        new_path = file.parent / new_name

        if dry_run:
            print(f"[預覽] {file.name} → {new_name}")
        else:
            file.rename(new_path)
            print(f"✓ {file.name} → {new_name}")


def main():
    parser = argparse.ArgumentParser(description="批次重命名工具")
    parser.add_argument("folder", help="資料夾路徑")
    parser.add_argument("--prefix", default="", help="檔名前綴")
    parser.add_argument("--ext", default="", help="副檔名，例如 .jpg")
    parser.add_argument("--dry-run", action="store_true", help="預覽模式")

    args = parser.parse_args()
    rename_files(args.folder, args.prefix, args.ext, args.dry_run)


if __name__ == "__main__":
    main()
