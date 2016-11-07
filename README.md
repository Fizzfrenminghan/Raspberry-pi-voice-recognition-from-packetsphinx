# Raspberry-pi-voice-recognition-from-packetsphinx
First $ sudo -i    go to root且SD卡的imag為原生Debian Wheezy,且先不要插入usb音效裝置                                                        

1.# apt-get update                                                                                                           
  # apt-get upgrade                                                                                                                                          
2.# wget http://goo.gl/1BOfJ -O /usr/bin/rpi-update && chmod +x /usr/bin/rpi-update                                         
  # apt-get install git-core                                                                                                 
  # sudo rpi-update                                                                                                         
  plug in your usb audio adapter 插入usb音效裝置                                                                               
  # cat /proc/asound/cards                                                                                                   
  # cat /proc/asound/modules                                                                                                  
  
3.# nano /etc/modprobe.d/alsa-base.conf                                                                                     
    更改/etc/modprobe.d/alsa-base.conf裡的                                                                                     
    options snd-usb-audio index=-2 改成 options snd-usb-audio index=0
    存檔後
  # alsa force-reload 強制重新載入ALSA
  # arecord -d 5 -r 48000 test.wav   To record 5secs sound test mic
  # aplay test.wav
  # alsamixer   Adjust input/output levele 
4.重要是要先安裝下面ALSA開發套件,不可先安裝sphinxbase,不然sphinxbase仍無法使用ALSA
  # apt-get install bison
  # apt-get install libasound2-dev
5.安裝sphinxbase
  # cd ../home/pi/sphinxbase-0.8/ 
  # ./configure --enable-fixed
  # make
  # make install
  
6.安裝pocketsphinx
  # cd ../pocketsphinx-0.8/
  # ./configure
  # make
  # make install
7.# src/programs/pocketsphinx_continuous -samprate 12000  執行測試

ready....
 

8.若無法執行則先run下方的path
# export LD_LIBRARY_PATH=/usr/local/lib
# export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig

為提高辨識精度可以限制字詞：
例如先建立一個mark.txt(中文字一樣) :

hello
goodbye
music
picture
display
time
forward
right
left
back


然後開啟瀏覽器到此網址：http://www.speech.cs.cmu.edu/tools/lmtool-new.html
在Upload a sentence corpus file: 下方選擇檔案，選擇剛建立的mark.txt
再按COMPILE KNOWLEDGE BASE 跳出一個視窗再下載其中的例如：TAR7737.tga檔到 /pocketsphinx-0.8/src/programs裡
解壓TAR7737.tga檔 得到 例如： 7737.dic 7737.lm 等檔案,
(若是中文字部份，下載下來的3829.dic檔內無羅馬拼音,
須到/home/pi/pocketsphinx-0.8/model/lm/zh_TW/mandarin_notone.dic裡
找自己要的中文羅馬拼音，並複製貼於剛剛生成的3829.dic檔裡)
(然後到/home/pi/pocketsphinx-0.8/model/hmm/zh裡複製tdt_sc_8k資料夾到pocketsphinx_continuous同目錄)


在終端機輸入
./pocketsphinx_continuous -lm 7737.lm -dict 7737.dic
然後只辨識mark.txt裡的十個字
(中文辨識則輸入./pocketsphinx_continuous -hmm tdt_sc_8k -lm 3829.lm -dict 3829.dic)

若要執行自己的bash或python指令，則修改continuous.c裡的/* Exit if the first word spoken was GOODBYE */ 判斷式

如：

   if (hyp) {
            sscanf(hyp, "%s", word);
            if (strcmp(hyp, "GOODBYE") == 0)
               {
                system("espeak \"good bye\"");
                break;
               }
            else if (strcmp(hyp, "LEFT") == 0)
               {
                system("/home/pi/gpio/servol.py");
               }
            }

存檔後再執行make重新編譯continuous.c再建立一個 pocketsphinx_continuous新版本，可能有權限的問題，屆時要執行時前方再加sudo

reference: 
           http://www.raspberrypi-spy.co.uk/2013/01/cheap-pir-sensors-and-the-raspberry-pi-part-1/

video: 
           https://www.youtube.com/watch?v=EucxVToC58E&hd=1
           https://www.youtube.com/watch?v=2K2-8GRhIvw&hd=1


