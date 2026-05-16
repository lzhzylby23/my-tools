import argparse  # 招聘一位「收發員」，負責處理終端機傳進來的指令
import os  # 招聘一位「搬運工」，負責作業系統的檔案操作（改名、移動）

# 1. 叫「收發員」出來準備
parser = argparse.ArgumentParser(description="我的第一個自動改名機器人")

# 2. 定義它要收什麼指令
# 必填項：沒地址他就不出門
parser.add_argument("folder", help="你要改哪個資料夾的檔案？")
# 選填項：預設不加任何字，除非你指定 --prefix
parser.add_argument("--prefix", default="", help="檔名前面要加什麼字？")
# 選填項：如果指令裡有 --dry-run，他就只看不動手
parser.add_argument("--dry-run", action="store_true", help="只顯示結果，不真的改名")

# 3. 開始解析你打的字
args = parser.parse_args()

# 4. 程式邏輯（執行指令）
print(f"--- 準備處理資料夾：{args.folder} ---")

if args.dry_run:
    print("⚠️ 目前是【預覽模式】，檔案不會真的變動喔！")

# 測試看看能不能抓到資料夾裡的檔案
try:
    files = os.listdir(args.folder)
    for f in files:
        # 1. 算出舊的路徑與新的路徑
        old_path = os.path.join(args.folder, f)
        new_name = f"{args.prefix}{f}"
        new_path = os.path.join(args.folder, new_name)

        # 2. 判斷現在是「只說不做」還是「真的動手」
        if args.dry_run:
            print(f"[預覽模式] 把 {f} 改名為 -> {new_name}")
        else:
            # 🌟 這行才是「真正動手」的核心指令！
            # 它會去呼叫 Windows 或 Mac 的系統功能來改名
            os.rename(old_path, new_path)
            print(f"✅ 已成功改名：{f} -> {new_name}")

except FileNotFoundError:
    print("❌ 找不到這個資料夾，請確認路徑對不對！")
