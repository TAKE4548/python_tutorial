@rem encoding: cp932(shift-jis)
@echo off

rem �����`�F�b�N
if "%1" == "" (
    echo �r���h����t�@�C�����w�肵�Ă�������
    pause
    exit -1
)

rem �t�@�C���`�F�b�N
if "%~x1" neq ".c" (
    echo �t�@�C���`�����Ⴂ�܂�
    pause
    exit -1
)

rem �r���h���s
echo "building %~n1%~x1 -> %~n1.exe"
gcc %1 -o %~d1%~p1%~n1.exe --exec-charset=cp932

rem �G���[�o�Ă���~�߂�
if %errorlevel% == 0 (
    echo successful
) else (
    pause
)