rem D�]���T�[�o����邽�߁A�Ӑ}�I�ɃT�C�g�ɕ��ׂ�������B
rem Windows�ł͕W����WGET�ɑ���bitsadmin /TRANSFER���p�ӂ���Ă����B
rem Dos�U���݂����ɂȂ�̂�local�ȊO�Ŏg��Ȃ��łˁB


rem �ǂ̃T�[�o�ɕ��ׂ������邩�I����
set target=http://192.168.1.81/index.php
:set target=http://192.168.1.82/index.php
:set target=http://192.168.1.83/index.php

rem �ʂ�win�R���s���[�^�œ����悤�Ɋ��ϐ��𗘗p�����B
rem ���ϐ�%HOMEPATH%�́u\Users\���[�U�[���v�������őI��ł����B
set forward=C:%HOMEPATH%\Downloads\


for /l %%n in (1,1,10) do (

rem bitsadmin.exe /TRANSFER <�W���u���F�C�ӂ�OK> <�����[�gURL> <�_�E�����[�h��>
rem ����t�@�C�������Ə㏑���ɂȂ��ĕ�����ɂ����̂�loop�Ɏg���ϐ��Ńt�@�C������ς���悤�ɂ����B1.html,2.html�c
bitsadmin /TRANSFER tes %target% %forward%%%n.php

)

rem ���ʂ������悤��
pause

