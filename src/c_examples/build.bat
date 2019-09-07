@rem encoding: cp932(shift-jis)
@echo off

rem 引数チェック
if "%1" == "" (
    echo ビルドするファイルを指定してください
    pause
    exit -1
)

rem ファイルチェック
if "%~x1" neq ".c" (
    echo ファイル形式が違います
    pause
    exit -1
)

rem ビルド実行
echo "building %~n1%~x1 -> %~n1.exe"
gcc %1 -o %~d1%~p1%~n1.exe --exec-charset=cp932

rem エラー出てたら止める
if %errorlevel% == 0 (
    echo successful
) else (
    pause
)