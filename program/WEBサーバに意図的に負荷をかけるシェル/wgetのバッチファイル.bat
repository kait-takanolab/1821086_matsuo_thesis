rem D�]���T�[�o����邽�߁A�Ӑ}�I�ɃT�C�g�ɕ��ׂ�������B
rem Windows�ł͕W����WGET�ɑ���bitsadmin /TRANSFER���p�ӂ���Ă����B
rem Dos�U���݂����ɂȂ�̂�local�ȊO�Ŏg��Ȃ��łˁB
rem bitsadmin.exe /TRANSFER <�W���u���F�C�ӂ�OK> <�����[�gURL> <�_�E�����[�h��>
rem �ʂ�win�R���s���[�^�œ����悤�Ɋ��ϐ��𗘗p����
rem ���ϐ�%HOMEPATH%�́u\Users\���[�U�[���v�������őI��ł����B
rem ����t�@�C�������Ə㏑���ɂȂ��ĕ�����ɂ����̂�loop�Ɏg���ϐ��Ńt�@�C������ς���悤�ɂ����B1.html,2.html�c




set forward=C:%HOMEPATH%\Downloads\
for /l %%n in (1,1,10) do (

bitsadmin /TRANSFER tes http://kumasakasoukou.com/index.html %forward%%%n.html

)

pause

