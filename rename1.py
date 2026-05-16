import argparse

parser = argparse.ArgumentParser(description="批次重命名資料夾中的檔案")

# 必填的位置參數
parser.add_argument("folder", help="目標資料夾路徑")

# 選填參數（有預設值）
parser.add_argument("--prefix", default="", help="加在檔名前面的文字")
parser.add_argument("--ext", default="", help="只處理特定副檔名，例如 .jpg")

# 布林開關（不需要值，有它就是 True）
parser.add_argument("--dry-run", action="store_true", help="預覽模式，不實際改名")

args = parser.parse_args()
print(args.folder, args.prefix, args.dry_run)
