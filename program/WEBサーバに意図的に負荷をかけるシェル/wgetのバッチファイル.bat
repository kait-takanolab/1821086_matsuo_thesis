rem D�]���T�[�o����邽�߁A�Ӑ}�I�ɃT�C�g�ɕ��ׂ�������B
rem Windows�ł͕W����WGET�ɑ���bitsadmin /TRANSFER���p�ӂ���Ă����B
rem Dos�U���݂����ɂȂ�̂�local�ȊO�Ŏg��Ȃ��łˁB

rem bitsadmin.exe /TRANSFER <�W���u���F�C�ӂ�OK> <�����[�gURL> <�_�E�����[�h��>


rem %HOMEPATH%�͊��ϐ��u\Users\���[�U�[���v���R���s���[�^���ɕς��Ă����


:for /l %%n in (1,1,100000) do (
:bitsadmin /TRANSFER tes http://kumasakasoukou.com/index.html C:%HOMEPATH%\Downloads\index.html
:)


