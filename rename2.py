import click

# 先安裝：pip install click


@click.command()
@click.argument("folder")
@click.option("--prefix", default="", help="檔名前綴")
@click.option("--ext", default="", help="副檔名過濾")
@click.option("--dry-run", is_flag=True, help="預覽模式")
def rename(folder, prefix, ext, dry_run):
    """批次重命名資料夾中的檔案"""
    click.echo(f"處理資料夾：{folder}")
    if dry_run:
        click.secho("[預覽模式] 不會實際改名", fg="yellow")


if __name__ == "__main__":
    rename()
