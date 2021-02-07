import click


from softmock import index
from softmock.utils.version import version as VERSION
from softmock import clear


def version(ctx, param, value):
    if value:
        click.secho(f'version : {VERSION}')
        ctx.exit()


def clear_all(ctx, param, value):
    if value:
        clear()
        click.secho(f'已清除所有数据')
        ctx.exit()


@click.command()
@click.option('--version', '-v', is_flag=True, is_eager=True, expose_value=False, help='查看softmock版本信息', callback=version)
@click.option('--host', '-h', prompt='请输入要监听的host', help='监听的host')
@click.option('--clear-all', help='清理所有数据', is_flag=True, is_eager=True, expose_value=False, callback=clear_all)
def main(host):
    """
    录制接口，并mock数据！
    """
    index.launch(host)


main()
