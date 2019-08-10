#!/usr/bin/python
######################################
#mau ngapain???                      #
#recode!!!                           #
#malu sama umur woy                  #
#laskarLaskar-Muslim-Cyber.blogspot.com#
######################################
mess = """\x1b[1;92m
======================================================
\x1b[1;91m
            Creator script deface      
            
                Author:Mr.p3mu14
                
     thanks to :[span anon] [all member LMC]

                [all member PcT]
\x1b[1;92m
======================================================"""

print mess
print "\x1b[1;95mCreated by Mr.p3mu14"
title = raw_input("\x1b[1;94mJudul title: ")

heading = raw_input("\x1b[1;93mHacked by: ")

linkwa = raw_input("\x1b[1;92mtaruh link contacts : ")

background = raw_input("\x1b[1;91mlink background : ")

namaats = raw_input("\x1b[1;95mpesan di atas/hacked by: ")
pesansingkat = raw_input("\x1b[1;94mpesan singkat : ")
linkimg = raw_input("\x1b[1;93mlink gambar tengah : ")
pesan = raw_input("\x1b[1;92mpesan ,.gunakan <br>untuk membuat baris baru: ")
slogan = raw_input("\x1b[1;91mslogan/pesan singkat: ")
slogan2 = raw_input("\x1b[1;95mslogan ke2 : ")
musik = raw_input("\x1b[1;94mlink musik ,upload di top4top : ")
salam = raw_input("\x1b[1;93mucapan terimakasih : ")

#Open the index
fo = open("script.html","w")

script1 = """<html><head><title>"""

script2 = title

script3 = """</title>
<body>
<br>
<link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'>
<link href='http://fonts.googleapis.com/css?family=Anton' rel='stylesheet' type='text/css'> <font style="color:black;font size:8px;text-align: center;font-family:Pirata One;text-shadow: 0 0 10px #000000, 0px 0px 10px #000000,0 0 10px #000000,0 0 10px #000000;"><font face="Pirata One" color=red size=5><center>
<br>
<a href="""
script4 = linkwa
script5 = """><input type="button" value="Contact me" onclick="alert('Mungkin kita bisa berteman :)');" style="font-size:1em;background:yellow"></a>
<style type='text/css'>body{

background:url("""
script6 = background

script7 = """) repeat center center fixed black;
}
</style><iframe width="0" height="0" src="""
script23 = musik
script24 ="""
frameborder="0" allowfullscreen></iframe>
</head>
<div class="dd-postmetadataheader">
<h2 class="dd-postheader">"""
script8 = """
</title><font size="10" face="Keania One" color="red">"""

script9 = namaats



script10 = """</font>
<center><font size="4" face="Narkisim" color="38df21">"""

script11 = pesansingkat

script12 = """</font>
<script language=JavaScript></script>

<!--Simply copy and paste to the <head> section of your page.-->

 <!-- Color Skings CSS -->


<!-- /Color Skings CSS -->
<!-- Sketch BG-Gallery Starts Here -->  <script type="text/javascript">
   jQuery(document).ready(function(){
    jQuery.skebggallery('#skebggallery',{
     'delay':7500, 
     'fadeSpeed': 8000,
     'navigation':1,
     'playPause':1,
     'thumbnails':1,
     'thumb_':'square'
    });
    
    if(jQuery('#skebggallery_cap').length > 0){
     jQuery.skebggcaptions('#skebggallery_cap',{
      'delay':8500, 
      'fadeSpeed': 8000     });
    }
   });
  </script>
     <div id="skebggallery">
<img src="""
script13 = linkimg
script14 = """ border="0"width="450px" height="460px"></img><div class="skebg_overlay" style="background:url('http://shop4brides.ru/wp-content/themes/irex-lite/images/sketchbg/overlay/01.png"')/>
</div>
</div>
<body>
<body onkeydown="return false">
</SCRIPT>


</SCRIPT>
<layer z-Index=2>
<div  style="position: relative">

<layer z-Index=2>
<div style="position: relative">

</SCRIPT>
<link href="http://fonts.googleapis.com/css?family=Iceland" rel="stylesheet" type="text/css">
<p align
<SCRIPT language="JavaScript">
<center>
<font color="green">
<embed name=""
src=""
loop="true"
hidden="true"
autostart="true">
</embed>
<center>
<script type="text/javascript">
// Hacked By : S3cvr1Ty H4ck3r
TypingText = function(element, interval, cursor, finishedCallback) {
  if((typeof document.getElementById == "undefined") || (typeof element.innerHTML == "undefined")) {
    this.running = true;
    return;
  }
  this.element = element;
  this.finishedCallback = (finishedCallback ? finishedCallback : function() { return; });
  this.interval = (typeof interval == "undefined" ? 100 : interval);
  this.origText = this.element.innerHTML;
  this.unparsedOrigText = this.origText;
  this.cursor = (cursor ? cursor : "");
  this.currentText = "";
  this.currentChar = 0;
  this.element.typingText = this;
  if(this.element.id == "") this.element.id = "typingtext" + TypingText.currentIndex++;
  TypingText.all.push(this);
  this.running = false;
  this.inTag = false;
  this.tagBuffer = "";
  this.inHTMLEntity = false;
  this.HTMLEntityBuffer = "";
}
TypingText.all = new Array();
TypingText.currentIndex = 0;
TypingText.runAll = function() {
  for(var i = 0; i < TypingText.all.length; i++) TypingText.all[i].run();
}
TypingText.prototype.run = function() {
  if(this.running) return;
  if(typeof this.origText == "undefined") {
    setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);
    return;
  }
  if(this.currentText == "") this.element.innerHTML = "";
  if(this.currentChar < this.origText.length) {
    if(this.origText.charAt(this.currentChar) == "<" && !this.inTag) {
      this.tagBuffer = "<";
      this.inTag = true;
      this.currentChar++;
      this.run();
      return;
    } else if(this.origText.charAt(this.currentChar) == ">" && this.inTag) {
      this.tagBuffer += ">";
      this.inTag = false;
      this.currentText += this.tagBuffer;
      this.currentChar++;
      this.run();
      return;
    } else if(this.inTag) {
      this.tagBuffer += this.origText.charAt(this.currentChar);
      this.currentChar++;
      this.run();
      return;
    } else if(this.origText.charAt(this.currentChar) == "&" && !this.inHTMLEntity) {
      this.HTMLEntityBuffer = "&";
      this.inHTMLEntity = true;
      this.currentChar++;
      this.run();
      return;
    } else if(this.origText.charAt(this.currentChar) == ";" && this.inHTMLEntity) {
      this.HTMLEntityBuffer += ";";
      this.inHTMLEntity = false;
      this.currentText += this.HTMLEntityBuffer;
      this.currentChar++;
      this.run();
      return;
    } else if(this.inHTMLEntity) {
      this.HTMLEntityBuffer += this.origText.charAt(this.currentChar);
      this.currentChar++;
      this.run();
      return;
    } else {
      this.currentText += this.origText.charAt(this.currentChar);
    }
    this.element.innerHTML = this.currentText;
    this.element.innerHTML += (this.currentChar < this.origText.length - 1 ? (typeof this.cursor == "function" ? this.cursor(this.currentText) : this.cursor) : "");
    this.currentChar++;
    setTimeout("document.getElementById('" + this.element.id + "').typingText.run()", this.interval);
  } else {
    this.currentText = "";
    this.currentChar = 0;
        this.running = false;
        this.finishedCallback();
  }
}

</script>

<center>
<p id="message">
<font size="3" face="Narkisim" color="38df21">
[+] ^^ Message Begins ^^ [+]
<br>
<font size="5" face="Narkisim" color="red">
------------------------------
<br>
<font size="3" face="Narkisim" color="white">"""
script15 = pesan

script16 = """<br>
<font size="5" face="Narkisim" color="red">
---------------------------------------------------------------------------
<br>
<font size="3" face="Narkisim" color="white">"""
script17 = slogan
script18 = """ <br>
<font size="5" face="Narkisim" color="red">
-------------------
<br> 
<font size="5" face="Narkisim" color="red">"""
script19 = slogan2
script20 = """<br/> 

<font color="white">?<font color="38df21"> ?
</div></div>
<script type="text/javascript">
new TypingText(document.getElementById("message"), 55, function(i){ var ar = new Array("|", "|", "|", "|"); return " " + ar[i.length % ar.length]; });

//Type out examples:
TypingText.runAll();

</script><center>
<br>


<body background="">


</script>
<link href='http://fonts.googleapis.com/css?family=Keania+One' rel='stylesheet' type='text/css'>

<font size="4" face="Narkisim" color="orange">~: [+] We Will Come Back [+] :~<br>
</font><font size="7" face="Keania One" color="red">You<font color="white"> Got <font color="38df21">Hacked

<style type="text/css">
.absoluta {position: absolute;
bottom: 0;
right: 0;
background-color: #000;
color: #fff;
}

</style>
<link href='http://fonts.googleapis.com/css?family=Iceland' rel='stylesheet' type='text/css'>
<font face="Iceland" size="4">
<br><br><font face="Iceland" size="4"><marquee scrollamount="3" scrolldelay="50" width="80%">
<font color="orange" face="Colonna MT" size="6"> [+] Greetz to  >"""
script21 = salam
script22 = """[+]  
</font></marquee></font></p>
<center>
<iframe width="0%" height="0" scrolling="no" frameborder="no" src="https://www.youtube.com/v/9O72RLP5fF4?rel=0&autoplay=1&showsearch=0></center>
<body bgcolor="black" oncontextmenu="return false" onkeydown="return false">



</div>
</body>

</html><script Language=VBScript><!--

//--></SCRIPT>"""


fo.write(script1)
fo.write(script2)
fo.write(script3)
fo.write(script4)
fo.write(script5)
fo.write(script6)
fo.write(script7)
fo.write(script23)
fo.write(script24)
fo.write(script8)
fo.write(script9)
fo.write(script10)
fo.write(script11)
fo.write(script12)
fo.write(script13)
fo.write(script14)
fo.write(script15)
fo.write(script16)
fo.write(script17)
fo.write(script18)
fo.write(script19)
fo.write(script20)
fo.write(script21)
fo.write(script22)





print "\x1b[1;92mScript Berhasil Di buat!"
print "enjoyyyy"

fo.close()