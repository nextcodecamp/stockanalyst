from shiny import ui, render, App,reactive
from matplotlib import pyplot as plt
#https://ayz61y-nextcode-camp.shinyapps.io/shinypython/
#Stock analyst
import math 
import pandas as pd
import pandas_ta as ta
import yfinance as yf
#import seaborn as sns
import numpy as np
style="border: none;"

app_ui = ui.page_fluid(
   
    #ui.img(src='next.jpg', align = "left", width="100", height="100"),
    ui.row(ui.column(1, ui.output_image("image"), style="padding-top:0px"),ui.column(10, ui.h1("Next2U: Stock Analyst for You"),) , style = "padding-top:10px;height:80px; background-color: yellow;"),
    
    ui.row(
          ui.column(3,ui.input_selectize( "stock","Choose a stock:",
                              {
                                "RESOURCE":
  {"7UP.BK":"7UP","ABM.BK":"ABM","ACC.BK":"ACC","ACE.BK":"ACE","AGE.BK":"AGE","AI.BK":"AI","AIE.BK":"AIE","AKR.BK":"AKR",
         "BAFS.BK":"BAFS","BANPU.BK":"BANPU","BBGI.BK":"BBGI","BCP.BK":"BCP","BCPG.BK":"BCPG","BGRIM.BK":"BGRIM",
                              "BIOTEC.BK":"BIOTEC","BPP.BK":"BPP","BRRGIF.BK":"BRRGIF","BSRC.BK":"BSRC","CKP.BK":"CKP","CV.BK":"CV",
                              "DEMCO.BK":"DEMCO","EA.BK":"EA","EASTW.BK":"EASTW","EGATIF.BK":"EGATIF","EGCO.BK":"EGCO",
"EP.BK":"EP","ETC.BK":"ETC","GPSC.BK":"GPSC","GREEN.BK":"GREEN","GTV.BK":"GTV","GULF.BK":"GULF","GUNKUL.BK":"GUNKUL","IFEC.BK":"IFEC",
"IRPC.BK":"IRPC","JR.BK":"JR","KBSPIF.BK":"KBSPIF","LANNA.BK":"LANNA","MDX.BK":"MDX","NOVA.BK":"NOVA","OR.BK":"OR","PCC.BK":"PCC","PRIME.BK":"PRIME",
"PSTC.BK":"PSTC","PTC.BK":"PTC","PTG.BK":"PTG","PTT.BK":"PTT","PTTEP.BK":"PTTEP","QTC.BK":"QTC","RATCH.BK":"RATCH","RPC.BK":"RPC","SAAM.BK":"SAAM","SCG.BK":"SCG","SCI.BK":"SCI","SCN.BK":"SCN","SEAOIL.BK":"SEAOIL","SGP.BK":"SGP","SKE.BK":"SKE","SOLAR.BK":"SOLAR","SPCG.BK":"SPCG",
"SPRC.BK":"SPRC","SR.BK":"SR","SSP.BK":"SSP","STOWER.BK":"STOWER","SUPER.BK":"SUPER","SUPEREIF.BK":"SUPEREIF","SUSCO.BK":"SUSCO","TAE.BK":"TAE","TAKUNI.BK":"TAKUNI","TCC.BK":"TCC","TGE.BK":"TGE",
"TOP.BK":"TOP","TPCH.BK":"TPCH","TPIPP.BK":"TPIPP","TRT.BK":"TRT","TSE.BK":"TSE","TTW.BK":"TTW","UBE.BK":"UBE","UMS.BK":"UMS","WHAUP.BK":"WHAUP","WP.BK":"WP"},
               
                          
                          "AGRO":{
"AAI.BK":"AAI","APURE.BK":"APURE","ASIAN.BK":"ASIAN","AU.BK":"AU","BR.BK":"BR","BRR.BK":"BRR","BTG.BK":"BTG",
"CBG.BK":"CBG","CFRESH.BK":"CFRESH","CH.BK":"CH","CHOTI.BK":"CHOTI","CM.BK":"CM","COCOCO.BK":"COCOCO",
"CPF.BK":"CPF","CPI.BK":"CPI","EE.BK":"EE","F&D.BK":"F&D","GFPT.BK":"GFPT","GLOCON.BK":"GLOCON",
"HTC.BK":"HTC","ICHI.BK":"ICHI","ITC.BK":"ITC","JCKH.BK":"JCKH","JDF.BK":"JDF","KASET.BK":"KASET",
"KBS.BK":"KBS","KCG.BK":"KCG","KSL.BK":"KSL","KTIS.BK":"KTIS","LEE.BK":"LEE","LST.BK":"LST","M.BK":"M",
"MALEE.BK":"MALEE","MAX.BK":"MAX","MUD.BK":"MUD","NER.BK":"NER","NRF.BK":"NRF","NSL.BK":"NSL","NTSC.BK":"NTSC","OSP.BK":"OSP",
"PB.BK":"PB","PLUS.BK":"PLUS","PM.BK":"PM","PPPM.BK":"PPPM","PQS.BK":"PQS","PRG.BK":"PRG","RBF.BK":"RBF","SAPPE.BK":"SAPPE",
"SAUCE.BK":"SAUCE","SNNP.BK":"SNNP","SNP.BK":"SNP","SORKON.BK":"SORKON","SSC.BK":"SSC","SSF.BK":"SSF","SST.BK":"SST","STA.BK":"STA","SUN.BK":"SUN","TACC.BK":"TACC","TC.BK":"TC","TEGH.BK":"TEGH","TFG.BK":"TFG","TFM.BK":"TFM","TFMAMA.BK":"TFMAMA","TIPCO.BK":"TIPCO","TKN.BK":"TKN","TMILL.BK":"TMILL","TRUBB.BK":"TRUBB","TU.BK":"TU","TVO.BK":"TVO","TWPC.BK":"TWPC","UPOIC.BK":"UPOIC","UVAN.BK":"UVAN","VPO.BK":"VPO","W.BK":"W","WINNER.BK":"WINNER","XO.BK":"XO","ZEN.BK":"ZEN",

                          },
                          "CONSUMPTION":
{"AFC.BK":"AFC","AJA.BK":"AJA","ALPHAX.BK":"ALPHAX","APCO.BK":"APCO","AURA.BK":"AURA","BGT.BK":"BGT","BIZ.BK":"BIZ","BLC.BK":"BLC","BTNC.BK":"BTNC","CPH.BK":"CPH","CPL.BK":"CPL","DDD.BK":"DDD","DOD.BK":"DOD","DTCI.BK":"DTCI","ECF.BK":"ECF","EFORL.BK":"EFORL","FANCY.BK":"FANCY","FTI.BK":"FTI","HPT.BK":"HPT","IP.BK":"IP","ITTHI.BK":"ITTHI",
"JCT.BK":"JCT","JSP.BK":"JSP","JUBILE.BK":"JUBILE","KISS.BK":"KISS","KYE.BK":"KYE","L&E.BK":"L&E","MODERN.BK":"MODERN","MOONG.BK":"MOONG","NAM.BK":"NAM","NC.BK":"NC","NPK.BK":"NPK","NV.BK":"NV","OCC.BK":"OCC","OGC.BK":"OGC","PAF.BK":"PAF","PDJ.BK":"PDJ","PG.BK":"PG","ROCK.BK":"ROCK","S&J.BK":"S&J","SABINA.BK":"SABINA","SAWANG.BK":"SAWANG","SBNEXT.BK":"SBNEXT","SIAM.BK":"SIAM",
"SMD.BK":"SMD","STGT.BK":"STGT","STHAI.BK":"STHAI","SUC.BK":"SUC","TCMC.BK":"TCMC","TM.BK":"TM","TNL.BK":"TNL","TNR.BK":"TNR","TOG.BK":"TOG","TR.BK":"TR","TTI.BK":"TTI","TTT.BK":"TTT",
"UPF.BK":"UPF","WACOAL.BK":"WACOAL","WARRIX.BK":"WARRIX","WFX.BK":"WFX","WINMED.BK":"WINMED"},
"FINANCE":
{"ACAP.BK":"ACAP","AEONTS.BK":"AEONTS","AF.BK":"AF","AIRA.BK":"AIRA","AMANAH.BK":"AMANAH","ASAP.BK":"ASAP",
"ASK.BK":"ASK","ASN.BK":"ASN","ASP.BK":"ASP","AYUD.BK":"AYUD","BAM.BK":"BAM","BAY.BK":"BAY","BBL.BK":"BBL","BKI.BK":"BKI","BLA.BK":"BLA","BROOK.BK":"BROOK","BUI.BK":"BUI","BYD.BK":"BYD",
"CGH.BK":"CGH","CHARAN.BK":"CHARAN","CHASE.BK":"CHASE","CHAYO.BK":"CHAYO","CIMBT.BK":"CIMBT","ECL.BK":"ECL","FNS.BK":"FNS","FSX.BK":"FSX",
"GBX.BK":"GBX","GCAP.BK":"GCAP","GL.BK":"GL","HENG.BK":"HENG","IFS.BK":"IFS","INSURE.BK":"INSURE","JMT.BK":"JMT","KBANK.BK":"KBANK",
"KCAR.BK":"KCAR","KCC.BK":"KCC","KGI.BK":"KGI","KKP.BK":"KKP","KTB.BK":"KTB","KTC.BK":"KTC","KWI.BK":"KWI","LHFG.BK":"LHFG",
"LIT.BK":"LIT","MFC.BK":"MFC","MICRO.BK":"MICRO","MITSIB.BK":"MITSIB","ML.BK":"ML","MST.BK":"MST","MTC.BK":"MTC","MTI.BK":"MTI",
"NCAP.BK":"NCAP","NKI.BK":"NKI","PL.BK":"PL","S11.BK":"S11","SAK.BK":"SAK","SAWAD.BK":"SAWAD","SCAP.BK":"SCAP","SCB.BK":"SCB",
"SGC.BK":"SGC","SGF.BK":"SGF","SM.BK":"SM","SMK.BK":"SMK","TCAP.BK":"TCAP","TGH.BK":"TGH","TH.BK":"TH","THANI.BK":"THANI",
"THRE.BK":"THRE","THREL.BK":"THREL","TIDLOR.BK":"TIDLOR","TIPH.BK":"TIPH","TISCO.BK":"TISCO","TK.BK":"TK","TLI.BK":"TLI","TNITY.BK":"TNITY",
"TQM.BK":"TQM","TQR.BK":"TQR","TSI.BK":"TSI","TTB.BK":"TTB","TVH.BK":"TVH","UOBKH.BK":"UOBKH","XPG.BK":"XPG"},

"INDUSTRY":   {   "2S.BK":"2S","3K-BAT.BK":"3K-BAT","ACG.BK":"ACG","ADB.BK":"ADB","AH.BK":"AH","AJ.BK":"AJ","ALLA.BK":"ALLA",
"ALUCON.BK":"ALUCON","AMC.BK":"AMC","ASEFA.BK":"ASEFA","BCT.BK":"BCT","BGC.BK":"BGC","BM.BK":"BM","BSBM.BK":"BSBM","CEN.BK":"CEN","CHO.BK":"CHO","CHOW.BK":"CHOW","CIG.BK":"CIG","CITY.BK":"CITY","CMAN.BK":"CMAN",
"COLOR.BK":"COLOR","CPR.BK":"CPR","CPT.BK":"CPT","CRANE.BK":"CRANE","CSC.BK":"CSC","CSP.BK":"CSP","CTW.BK":"CTW","CWT.BK":"CWT","EASON.BK":"EASON","FMT.BK":"FMT","FPI.BK":"FPI","GC.BK":"GC","GGC.BK":"GGC","GIFT.BK":"GIFT","GJS.BK":"GJS",
"GSTEEL.BK":"GSTEEL","GTB.BK":"GTB","GYT.BK":"GYT","HFT.BK":"HFT","HTECH.BK":"HTECH","IHL.BK":"IHL","INGRS.BK":"INGRS","INOX.BK":"INOX","IRC.BK":"IRC","IVL.BK":"IVL","KCM.BK":"KCM","KJL.BK":"KJL",
"KKC.BK":"KKC","KUMWEL.BK":"KUMWEL","KWM.BK":"KWM","LHK.BK":"LHK","MBAX.BK":"MBAX","MCS.BK":"MCS","MGC.BK":"MGC","MGT.BK":"MGT","MILL.BK":"MILL","MTW.BK":"MTW","NDR.BK":"NDR","NEP.BK":"NEP","NEX.BK":"NEX",
"NFC.BK":"NFC","PACO.BK":"PACO","PAP.BK":"PAP","PATO.BK":"PATO","PCSGH.BK":"PCSGH","PDG.BK":"PDG","PERM.BK":"PERM","PIMO.BK":"PIMO","PJW.BK":"PJW",
"PK.BK":"PK","PMTA.BK":"PMTA","POLY.BK":"POLY","PPM.BK":"PPM","PRAPAT.BK":"PRAPAT","PSP.BK":"PSP","PTL.BK":"PTL",
"PTTGC.BK":"PTTGC","RWI.BK":"RWI","SAF.BK":"SAF","SALEE.BK":"SALEE","SAM.BK":"SAM","SANKO.BK":"SANKO","SAT.BK":"SAT",
"SCGP.BK":"SCGP","SCL.BK":"SCL","SELIC.BK":"SELIC","SFLEX.BK":"SFLEX","SFT.BK":"SFT","SITHAI.BK":"SITHAI","SLP.BK":"SLP","SMIT.BK":"SMIT","SMPC.BK":"SMPC","SNC.BK":"SNC",
"SPACK.BK":"SPACK","SPG.BK":"SPG","SSSC.BK":"SSSC","STANLY.BK":"STANLY","STARK.BK":"STARK","STP.BK":"STP",
"SUTHA.BK":"SUTHA","SWC.BK":"SWC","TCJ.BK":"TCJ","TCOAT.BK":"TCOAT","TFI.BK":"TFI","TGPRO.BK":"TGPRO",
"THE.BK":"THE","THIP.BK":"THIP","TKT.BK":"TKT","TMC.BK":"TMC","TMD.BK":"TMD","TMI.BK":"TMI","TMT.BK":"TMT","TMW.BK":"TMW",
"TNPC.BK":"TNPC","TOPP.BK":"TOPP","TPA.BK":"TPA","TPAC.BK":"TPAC","TPBI.BK":"TPBI","TPCS.BK":"TPCS","TPLAS.BK":"TPLAS","TPP.BK":"TPP",
"TRU.BK":"TRU","TRV.BK":"TRV","TSC.BK":"TSC","TSTH.BK":"TSTH","TWP.BK":"TWP","TYCN.BK":"TYCN","UAC.BK":"UAC","UBIS.BK":"UBIS",
"UEC.BK":"UEC","UKEM.BK":"UKEM","UP.BK":"UP","UREKA.BK":"UREKA","UTP.BK":"UTP","VARO.BK":"VARO","YUASA.BK":"YUASA","ZIGA.BK":"ZIGA"},   
"PROPERTY":{
"24CS.BK":"24CS","A.BK":"A","A5.BK":"A5","AIMCG.BK":"AIMCG","AIMIRT.BK":"AIMIRT","AKS.BK":"AKS","ALL.BK":"ALL","ALLY.BK":"ALLY","AMATA.BK":"AMATA",
"AMATAR.BK":"AMATAR","AMATAV.BK":"AMATAV","ANAN.BK":"ANAN","AP.BK":"AP","APCS.BK":"APCS","APEX.BK":"APEX","ARIN.BK":"ARIN","ARROW.BK":"ARROW","ASW.BK":"ASW","AWC.BK":"AWC","B-WORK.BK":"B-WORK","BAREIT.BK":"BAREIT","BC.BK":"BC",
"BJCHI.BK":"BJCHI","BKD.BK":"BKD","BKKCP.BK":"BKKCP","BLAND.BK":"BLAND","BLESS.BK":"BLESS","BOFFICE.BK":"BOFFICE","BRI.BK":"BRI","BROCK.BK":"BROCK",
"BSM.BK":"BSM","BTW.BK":"BTW","CAZ.BK":"CAZ","CCP.BK":"CCP","CGD.BK":"CGD","CHEWA.BK":"CHEWA","CI.BK":"CI","CIVIL.BK":"CIVIL","CK.BK":"CK",
"CMC.BK":"CMC","CNT.BK":"CNT","COTTO.BK":"COTTO","CPANEL.BK":"CPANEL","CPN.BK":"CPN","CPNCG.BK":"CPNCG","CPNREIT.BK":"CPNREIT","CPTGF.BK":"CPTGF","CRD.BK":"CRD","CTARAF.BK":"CTARAF","DCC.BK":"DCC","DCON.BK":"DCON","DHOUSE.BK":"DHOUSE","DIMET.BK":"DIMET",
"DPAINT.BK":"DPAINT","DREIT.BK":"DREIT","DRT.BK":"DRT","EMC.BK":"EMC","EPG.BK":"EPG","ERWPF.BK":"ERWPF","ESTAR.BK":"ESTAR","EVER.BK":"EVER","FLOYD.BK":"FLOYD","FPT.BK":"FPT","FTREIT.BK":"FTREIT","FUTUREPF.BK":"FUTUREPF","GAHREIT.BK":"GAHREIT","GEL.BK":"GEL",
"GLAND.BK":"GLAND","GROREIT.BK":"GROREIT","GVREIT.BK":"GVREIT","HPF.BK":"HPF","HYDRO.BK":"HYDRO","HYDROGEN.BK":"HYDROGEN","IMPACT.BK":"IMPACT","IND.BK":"IND",
"INETREIT.BK":"INETREIT","ITD.BK":"ITD","J.BK":"J","JAK.BK":"JAK","JCK.BK":"JCK","K.BK":"K","KC.BK":"KC","KPNPF.BK":"KPNPF","KTBSTMR.BK":"KTBSTMR","KUN.BK":"KUN",
"LALIN.BK":"LALIN","LH.BK":"LH","LHHOTEL.BK":"LHHOTEL","LHPF.BK":"LHPF","LHSC.BK":"LHSC","LPF.BK":"LPF","LPN.BK":"LPN",
"LUXF.BK":"LUXF","M-II.BK":"M-II","M-PAT.BK":"M-PAT","M-STOR.BK":"M-STOR","MBK.BK":"MBK","META.BK":"META","MIPF.BK":"MIPF",
"MIT.BK":"MIT","MJD.BK":"MJD","MJLF.BK":"MJLF","MK.BK":"MK","MNIT.BK":"MNIT","MNIT2.BK":"MNIT2","MNRF.BK":"MNRF","NCH.BK":"NCH",
"NNCL.BK":"NNCL","NOBLE.BK":"NOBLE","NUSA.BK":"NUSA","NVD.BK":"NVD","NWR.BK":"NWR","ORI.BK":"ORI","ORN.BK":"ORN","PACE.BK":"PACE","PEACE.BK":"PEACE",
"PF.BK":"PF","PIN.BK":"PIN","PLAT.BK":"PLAT","PLE.BK":"PLE","POLAR.BK":"POLAR","POPF.BK":"POPF","PPF.BK":"PPF","PPP.BK":"PPP","PPS.BK":"PPS","PREB.BK":"PREB",
"PRECHA.BK":"PRECHA","PRI.BK":"PRI","PRIN.BK":"PRIN","PROS.BK":"PROS","PROSPECT.BK":"PROSPECT","PROUD.BK":"PROUD","PSG.BK":"PSG","PSH.BK":"PSH","PYLON.BK":"PYLON","Q-CON.BK":"Q-CON",
"QH.BK":"QH","QHHR.BK":"QHHR","QHOP.BK":"QHOP","QHPF.BK":"QHPF","RABBIT.BK":"RABBIT","RICHY.BK":"RICHY","RML.BK":"RML","ROJNA.BK":"ROJNA","RT.BK":"RT","S.BK":"S",
"SA.BK":"SA","SAMCO.BK":"SAMCO","SC.BK":"SC","SCC.BK":"SCC","SCCC.BK":"SCCC","SCP.BK":"SCP","SEAFCO.BK":"SEAFCO","SENA.BK":"SENA",
"SENX.BK":"SENX","SIRI.BK":"SIRI","SIRIP.BK":"SIRIP","SK.BK":"SK","SKN.BK":"SKN","SMART.BK":"SMART","SPALI.BK":"SPALI",
"SPRIME.BK":"SPRIME","SQ.BK":"SQ","SRICHA.BK":"SRICHA","SRIPANWA.BK":"SRIPANWA","SSPF.BK":"SSPF","SSS.BK":"SSS","SSTRT.BK":"SSTRT",
"STC.BK":"STC","STEC.BK":"STEC","STECH.BK":"STECH","STI.BK":"STI","STPI.BK":"STPI","SVR.BK":"SVR","SYNTEC.BK":"SYNTEC","TAPAC.BK":"TAPAC",
"TASCO.BK":"TASCO","TEAMG.BK":"TEAMG","TEKA.BK":"TEKA","THANA.BK":"THANA","TIF1.BK":"TIF1","TIGER.BK":"TIGER","TITLE.BK":"TITLE",
"TLHPF.BK":"TLHPF","TNPF.BK":"TNPF","TOA.BK":"TOA","TPIPL.BK":"TPIPL","TPOLY.BK":"TPOLY","TPRIME.BK":"TPRIME","TRC.BK":"TRC",
"TRITN.BK":"TRITN","TTCL.BK":"TTCL","TTLPF.BK":"TTLPF","TU-PF.BK":"TU-PF","UMI.BK":"UMI","UNIQ.BK":"UNIQ","URBNPF.BK":"URBNPF",
"UV.BK":"UV","VNG.BK":"VNG","WGE.BK":"WGE","WHA.BK":"WHA","WHABT.BK":"WHABT","WHAIR.BK":"WHAIR","WHART.BK":"WHART","WIIK.BK":"WIIK","WIN.BK":"WIN",
"WINDOW.BK":"WINDOW","YONG.BK":"YONG"},

"SERVICE":{
  "AAV.BK":"AAV","ADD.BK":"ADD","AHC.BK":"AHC","AKP.BK":"AKP","AMA.BK":"AMA","AMARC.BK":"AMARC","AMARIN.BK":"AMARIN","AOT.BK":"AOT","AQUA.BK":"AQUA",
"ARIP.BK":"ARIP","AS.BK":"AS","ASIA.BK":"ASIA","ASIMAR.BK":"ASIMAR","ATP30.BK":"ATP30","AUCT.BK":"AUCT","B.BK":"B","B52.BK":"B52",
"BA.BK":"BA","BCH.BK":"BCH","BDMS.BK":"BDMS","BEAUTY.BK":"BEAUTY","BEC.BK":"BEC","BEM.BK":"BEM","BEYOND.BK":"BEYOND","BH.BK":"BH",
"BIG.BK":"BIG","BIS.BK":"BIS","BJC.BK":"BJC","BOL.BK":"BOL","BTS.BK":"BTS","BTSGIF.BK":"BTSGIF","BWG.BK":"BWG","CENTEL.BK":"CENTEL","CEYE.BK":"CEYE",
"CHG.BK":"CHG","CHIC.BK":"CHIC","CMO.BK":"CMO","CMR.BK":"CMR","COM7.BK":"COM7","CPALL.BK":"CPALL","CPAXT.BK":"CPAXT","CPW.BK":"CPW",
"CRC.BK":"CRC","CSR.BK":"CSR","CSS.BK":"CSS","D.BK":"D","DEXON.BK":"DEXON","DMT.BK":"DMT","DOHOME.BK":"DOHOME","DUSIT.BK":"DUSIT","DV8.BK":"DV8",
"EKH.BK":"EKH","ERW.BK":"ERW","ETE.BK":"ETE","ETL.BK":"ETL","FE.BK":"FE","FN.BK":"FN","FSMART.BK":"FSMART","FTE.BK":"FTE","FVC.BK":"FVC",
"GENCO.BK":"GENCO","GFC.BK":"GFC","GLOBAL.BK":"GLOBAL","GLORY.BK":"GLORY","GPI.BK":"GPI","GRAMMY.BK":"GRAMMY","GRAND.BK":"GRAND",
"GSC.BK":"GSC","HARN.BK":"HARN","HEALTH.BK":"HEALTH","HL.BK":"HL","HMPRO.BK":"HMPRO","ICC.BK":"ICC","III.BK":"III","ILM.BK":"ILM",
"IMH.BK":"IMH","IT.BK":"IT","JKN.BK":"JKN","JPARK.BK":"JPARK","KAMART.BK":"KAMART","KDH.BK":"KDH","KEX.BK":"KEX","KGEN.BK":"KGEN",
"KIAT.BK":"KIAT","KK.BK":"KK","KLINIQ.BK":"KLINIQ","KOOL.BK":"KOOL","KTMS.BK":"KTMS","KWC.BK":"KWC","LDC.BK":"LDC","LEO.BK":"LEO",
"LOXLEY.BK":"LOXLEY","LPH.BK":"LPH","LRH.BK":"LRH","M-CHAI.BK":"M-CHAI","MACO.BK":"MACO","MAJOR.BK":"MAJOR","MANRIN.BK":"MANRIN",
"MASTER.BK":"MASTER","MATCH.BK":"MATCH","MATI.BK":"MATI","MC.BK":"MC","MCA.BK":"MCA","MCOT.BK":"MCOT","MEB.BK":"MEB","MEGA.BK":"MEGA",
"MENA.BK":"MENA","MIDA.BK":"MIDA","MINT.BK":"MINT","MONO.BK":"MONO","MORE.BK":"MORE","MOSHI.BK":"MOSHI","MVP.BK":"MVP",
"NATION.BK":"NATION","NCL.BK":"NCL","NEW.BK":"NEW","NEWS.BK":"NEWS","NOK.BK":"NOK","NTV.BK":"NTV","NYT.BK":"NYT","OHTL.BK":"OHTL","ONEE.BK":"ONEE",
"OTO.BK":"OTO","PHG.BK":"PHG","PHOL.BK":"PHOL","PICO.BK":"PICO","PLANB.BK":"PLANB","PLT.BK":"PLT","PORT.BK":"PORT","POST.BK":"POST",
"PR9.BK":"PR9","PRAKIT.BK":"PRAKIT","PRINC.BK":"PRINC","PRM.BK":"PRM","PRO.BK":"PRO","PRTR.BK":"PRTR","PSL.BK":"PSL","PTECH.BK":"PTECH",
"QLT.BK":"QLT","RAM.BK":"RAM","RCL.BK":"RCL","RJH.BK":"RJH","ROH.BK":"ROH","RP.BK":"RP","RPH.BK":"RPH","RS.BK":"RS","RSP.BK":"RSP","SABUY.BK":"SABUY",
"SAFE.BK":"SAFE","SAV.BK":"SAV","SCM.BK":"SCM","SE.BK":"SE","SE-ED.BK":"SE-ED","SHANG.BK":"SHANG","SHR.BK":"SHR","SINGER.BK":"SINGER",
"SINO.BK":"SINO","SISB.BK":"SISB","SJWD.BK":"SJWD","SKR.BK":"SKR","SLM.BK":"SLM","SO.BK":"SO","SONIC.BK":"SONIC","SPA.BK":"SPA",
"SPC.BK":"SPC","SPI.BK":"SPI","SVT.BK":"SVT","TAN.BK":"TAN","TFFIF.BK":"TFFIF","THAI.BK":"THAI","THG.BK":"THG","THMUI.BK":"THMUI",
"TKS.BK":"TKS","TNDT.BK":"TNDT","TNH.BK":"TNH","TNP.BK":"TNP","TPL.BK":"TPL","TRP.BK":"TRP","TSTE.BK":"TSTE","TTA.BK":"TTA","TURTLE.BK":"TURTLE",
"TVDH.BK":"TVDH","TVT.BK":"TVT","UBA.BK":"UBA","VGI.BK":"VGI","VIBHA.BK":"VIBHA","VIH.BK":"VIH","VL.BK":"VL","VRANDA.BK":"VRANDA","WAVE.BK":"WAVE",
"WICE.BK":"WICE","WORK.BK":"WORK","WPH.BK":"WPH","YGG.BK":"YGG","ZAA.BK":"ZAA"

},
"TECHNOLOGY":{
"ADVANC.BK":"ADVANC","AIT.BK":"AIT","ALT.BK":"ALT","AMR.BK":"AMR","APP.BK":"APP","BBIK.BK":"BBIK","BE8.BK":"BE8","BLISS.BK":"BLISS","BVG.BK":"BVG","CCET.BK":"CCET","COMAN.BK":"COMAN","DELTA.BK":"DELTA","DIF.BK":"DIF","DITTO.BK":"DITTO","DTCENT.BK":"DTCENT",
"FORTH.BK":"FORTH","GABLE.BK":"GABLE","HANA.BK":"HANA","HUMAN.BK":"HUMAN","I2.BK":"I2","ICN.BK":"ICN","IIG.BK":"IIG","ILINK.BK":"ILINK","INET.BK":"INET","INSET.BK":"INSET","INTUCH.BK":"INTUCH","IRCP.BK":"IRCP",
"ITEL.BK":"ITEL","ITNS.BK":"ITNS","JAS.BK":"JAS","3BBIF.BK":"3BBIF","JMART.BK":"JMART","JTS.BK":"JTS","KCE.BK":"KCE","METCO.BK":"METCO","MFEC.BK":"MFEC","MSC.BK":"MSC","NETBAY.BK":"NETBAY","PLANET.BK":"PLANET",
"PROEN.BK":"PROEN","PT.BK":"PT","READY.BK":"READY","SAMART.BK":"SAMART","SAMTEL.BK":"SAMTEL","SDC.BK":"SDC","SECURE.BK":"SECURE","SICT.BK":"SICT",
"SIMAT.BK":"SIMAT","SIS.BK":"SIS","SKY.BK":"SKY","SMT.BK":"SMT","SPVI.BK":"SPVI","SRS.BK":"SRS","SVI.BK":"SVI","SVOA.BK":"SVOA","SYMC.BK":"SYMC",
"SYNEX.BK":"SYNEX","TBN.BK":"TBN","TEAM.BK":"TEAM","THCOM.BK":"THCOM","TKC.BK":"TKC","TPS.BK":"TPS","TRUE.BK":"TRUE","TWZ.BK":"TWZ",
"VCOM.BK":"VCOM",
},
                                  
 
                              },
                              multiple=True,
                              
                              selected="PTT.BK"
                              ) ),
          ui.column(2, ui.input_date("start","Start", value="2022-01-01"), style=style),
          ui.column(2, ui.input_date("end","End"), style=style),
          ui.column(1, ui.input_numeric("pct_chg", "Pct-chg:", 1, min=1, max=120)),
                              ui.column(1, ui.input_numeric("shf", "Shift:", 1, min=1, max=120)),
                              ui.column(1, ui.input_numeric("nday", "Days:", 14, min=1, max=365),
         
                              ),
                               
                               ui.column(1, ui.input_selectize("timef","Time frame:",
                              {
                                  "Freq": {"W":"W", "M":"M", "Q":"Q","Y":"Y"},
                                 
                                
                              },
                              multiple=False,
                              )),
                             
                              
                              ),
                              
                              
      
    ui.row(
    ui.column
    (12,
      
        ui.navset_tab(
          ui.nav_panel("Line",
                         ui.row(ui.column(2, ui.p("")),  ),
                         ui.row(  
                              ui.column(2, ui.input_checkbox("line", "Price", value=True)), 
                              ui.column(2, ui.input_checkbox("mo", "MO")), 
                              ui.column(2, ui.input_checkbox("sma", "SMA")), 
                              ui.column(2, ui.input_checkbox("ema", "EMA")),
                              ui.column(3,ui.input_action_button("goohlc", "See OHLC", class_="btn-success",style="padding-top:10px"))
                       
                             ),
                          ui.row(
                              ui.column(12, ui.output_plot("plotstock"))),
                        
                            ui.row(
                              ui.column(12, ui.output_table("getstock")))
                        ),
                         ui.nav_panel("Cycle",
                          ui.row(ui.column(1,ui.input_selectize("typecy","Ad.info:",
                             {"close":"Close", "return":"Return", "pctchg":"Pct-Chg"},
                              multiple=False, selected="close"
                              ) )),
                          ui.row(
                              ui.column(4, ui.output_plot("plotcycle1y")),
                              ui.column(4, ui.output_plot("plotcycle2y")),
                              ui.column(4, ui.output_plot("plotcycle3y"))),
                            ui.row(
                              ui.column(4, ui.output_plot("plotcycle4m")),
                              ui.column(4, ui.output_plot("plotcycle5m")),
                              ui.column(4, ui.output_plot("plotcycle6m"))),
                                ui.row(
                              ui.column(4, ui.output_plot("plotcycle1m")),
                              ui.column(4, ui.output_plot("plotcycle2m")),
                              ui.column(4, ui.output_plot("plotcycle3m"))),
                           
                        ), #End Cycle               
                     
              ui.nav_panel("MACD",
                        ui.row(
                            ui.column(1, ui.input_numeric("emafast", "fast:", 12, min=1, max=120)),
                              ui.column(1, ui.input_numeric("emaslow", "slow:", 26, min=1, max=365)),
                               ui.column(2, ui.input_selectize("tplot","Type plot:",
                              {
                                  "candle":"Candle", "line":"Line"
                                 
                                
                              },
                              multiple=False,selected="line"
                              )),
                        ),
                        ui.row(
                              ui.column(12, ui.output_plot("plotstockmacd")))
                        ), #End nav OHLC  
                       ui.nav_panel("Volatility",      
                          ui.row(  
                              ui.column(2, ui.input_checkbox("showclose", "Close")), 
                              ui.column(2, ui.input_checkbox("showvu", "Volatile-price (Up)")), 
                              ui.column(2, ui.input_checkbox("showvd", "Volatile-price (Down)")), 
                              
                              ui.column(2, ui.input_checkbox("showreturn", "Return")), 
                              
                              ui.column(2, ui.input_checkbox("showlog", "Log-return")), 
                              
                              ui.column(2, ui.input_checkbox("show30", "30 days")), 
                              ui.column(2, ui.input_checkbox("show60", "60 days")), 
                              
                             ),
                         ui.row(
                              ui.column(12, ui.output_plot("plotsdvolatile"))),
  
                         ui.row(ui.column(3,ui.input_action_button("gov", "Plot volatile all periods.", class_="btn-success",style="padding-top:10px")),
                         ui.column(3,ui.input_action_button("goboll", "Plot Bollinger Band.", class_="btn-success",style="padding-top:10px"))
                         ),
                         
                        ui.row(
                              ui.column(12, ui.output_plot("plotbollinger"))),
                            ui.row(
                              ui.column(4, ui.output_plot("plotcycle1yv")),
                              ui.column(4, ui.output_plot("plotcycle2yv")),
                              ui.column(4, ui.output_plot("plotcycle3yv"))),
                            ui.row(
                              ui.column(4, ui.output_plot("plotcycle4mv")),
                              ui.column(4, ui.output_plot("plotcycle5mv")),
                              ui.column(4, ui.output_plot("plotcycle6mv"))),
                                ui.row(
                              ui.column(4, ui.output_plot("plotcycle1mv")),
                              ui.column(4, ui.output_plot("plotcycle2mv")),
                              ui.column(4, ui.output_plot("plotcycle3mv"))),
                              
                        ),
          
                       
                      ui.nav_panel("Scatter",
                        ui.row(
                               ui.column(1, ui.input_selectize("scatter","Info:",
                              {
                                 "pct":"Pct-Chg", "volume":"Volume"
                                   },
                              multiple=False, selected="-"
                              )),),
                              
                           ui.row(
                              ui.column(12, ui.output_plot("plotscatter")))),  
                    
                     
                      ui.nav_panel("Candle",
                      ui.row(  
                              ui.column(2, ui.input_checkbox("canb", "Bollinger Band")), 
                              ui.column(2, ui.input_checkbox("cansma", "SMA")), 
                              ui.column(2, ui.input_checkbox("canema", "EMA")),
                              ui.column(2, ui.input_checkbox("strong", "Strong demand/suppy")),
                              
                             ),
                      ui.row(
                          ui.column(12, ui.output_plot("candleplot")),
                       ) 
                       
                      ),  #End candle
                      ui.nav_panel("Growth",
                      ui.row(
                          ui.column(12, ui.output_plot("normalizedplot")),
                       ) ,
                       ui.row(
                         ui.column(12, ui.output_plot("plothistory") )
                         
                       )
                       
                      ),  #End candle
                    
                        ui.nav_panel("Seasonality",
                           ui.row(
                             
                              ui.column(2, ui.input_selectize("period","Month:",
                              {
                                 "mo0": "-", "mo1":"January", "mo2":"February","mo3":"March", "mo4":"April","mo5":"May","mo6":"June","mo7":"July","mo8":"August","mo9":"September","mo10":"October",
                                 "mo11":"November","mo12":"December"
                              },
                              multiple=False, selected="mo0"
                              )) )
                           ,
                           ui.row(
                             
                              ui.column(12, ui.output_plot("plotseasonality")))),    
                    
                        ui.nav_panel("Sampling",
                           ui.row(
                              ui.column(12, ui.output_plot("plotsampling")))),    
                      ui.nav_panel("RSI",
                      ui.row(
                        ui.column(12, ui.output_plot("plotrsi" ))), 
                         #ui.row(
                               
                              # ui.column(12, ui.output_plot("testmotion"))
                          #   )
                            
                      ),  #End nav rsi
                      
                   ui.nav_panel("Correlation",
                       ui.row( ui.column(2, ui.input_selectize("idxcorr1","Indicator1", 
                                {
                                 "sma":"SMA", "rsi":"RSI","mom":"Momentum", "pctchg":"PCT-CHG","volume":"Volume"
                                   },
                              multiple=False, selected="sma"
                              )),
                       ui.column(2, ui.input_selectize("idxcorr2","Indicator2", 
                                {
                                 "sma":"SMA", "rsi":"RSI","mom":"Momentum", "pctchg":"PCT-CHG","volume":"Volume"
                                   },
                              multiple=False, selected="rsi"
                              )),
                                ui.column(2, ui.input_action_button("gocorr", "Find indicator correlation!", class_="btn-success",style="padding-top:10px")),
                                ui.column(2, ui.input_action_button("gocorrstock", "Find stock correlation!", class_="btn-success",style="padding-top:10px")),
                                
                              ),      
                                ui.row( ui.column(12,ui.output_plot("plotcorr"))),
                               ui.row( ui.column(12,ui.output_plot("plotcorrindicator"))),
                      
                     
                       ),
                  # ui.nav("History", ),
          ui.nav_panel("Support/Resistance",
                           ui.row(
                              ui.column(1, ui.input_checkbox("support", "Support")), 
                              ui.column(2, ui.input_checkbox("resistance", "Resistance")),
                              
                              ui.column(2, ui.input_numeric("line1", "Line1",30.0,min = 1.0, max=300.0)), 
                              ui.column(2, ui.input_numeric("line2", "Line2",35.0,min = 1.0, max=300.0)), 
                              ui.column(1, ui.input_checkbox("fibo1", "23.60%")),  #23.60%   38.2%, 50%, 61.8%, และ 78.6% 
                              ui.column(1, ui.input_checkbox("fibo2", "38.20%")),
                              ui.column(1, ui.input_checkbox("fibo3", "50.00%")),
                              ui.column(1, ui.input_checkbox("fibo4", "61.80%")),
                              ui.column(1, ui.input_checkbox("fibo5", "78.60%")),
                              
                              ),
                               ui.row(
                              
                              ui.column(12, ui.output_plot("plotsupport") )
                              ),
                             # ui.row( 
                             #ui.column(12, ui.output_table("tableshift") ),
                             
                            # ),
                              
          ),   
                   ui.nav_panel("Mean Reversion",
                   ui.row(
                              ui.column(1, ui.input_numeric("revema", "EMA-Days:", 200, min=1, max=365)), 
                              ui.column(1, ui.input_numeric("revsma", "SMA-Days:", 14, min=1, max=365))
                              ),
                               ui.row(
                              
                              ui.column(12, ui.output_plot("plotmeanrev") )
                              ),
                              
          ),  
          ui.nav_panel("Percent Change",
                   ui.row(
                              ui.column(1, ui.input_numeric("pchg", "Days:", 0, min=0, max=365)), 
                              ),
                   ui.row(
                              
                              ui.column(12, ui.output_plot("plotpchg") )
                              ),
                   ui.row(
                              
                              ui.column(12, ui.output_plot("plotbarpchg") )
                              ),
                              
          ),  
          ui.nav_panel("Return", 
                        ui.row(
                            ui.column(2, ui.input_selectize("rper","Period:",
                              {
                                 "1y":"1-year","2y":"2-year","3y":"3-year", 
                                 "1mo":"1-month","2mo":"2-month","3mo":"3-month","4mo":"4-month","5mo":"5-month","6mo":"6-month","7mo":"7-month","8mo":"8-month","9mo":"9-month",
                                 "10mo":"10-month","11mo":"11-month"
                                 },
                              multiple=False, selected="-"
                              )),
                              ui.column(2, ui.input_checkbox("logreturn", "Log Return")), 
                              ui.column(2, ui.input_checkbox("cumsum", "Cumulative Return")), 
                              ui.column(2, ui.input_checkbox("sdreturn", "Volatility")), 
                        ),
                        ui.row( 
                             ui.column(12, ui.output_plot("plotreturn") ),
                             
                             ),
                              ui.row( 
                             ui.column(12, ui.output_plot("plotreturnperiod") ),
                             
                             ),
                             ui.row( 
                             ui.column(12, ui.output_plot("plotreturnhis") ),
                             
                             ),
                            ) ,
                      
                 
                   ui.nav_panel("Dividend", 
                    ui.row(
                            ui.column(2, ui.input_selectize("perioddiv","Period:",
                              {
                                 "2024":"2024","2023":"2023","2022":"2022", 
                                 "2021":"2021","2020":"2020","2019":"2019", "all":"All"
                                 },
                              multiple=False, selected="all"
                              ))),
                         ui.row(
                            ui.column(12, ui.output_plot("plotdiv")))
                            ),
                              ui.nav_panel("Graph display",
                              ui.row(ui.column(12, ui.p(""))),
                         ui.row(
                             #ui.column(2, ui.input_checkbox("rmbg", "Remove background")),
                               ui.column(4, ui.input_checkbox("adbg", "Add background darkgrid"))
                             
                            ),
                             ui.row(
                              
                              ui.column(12, ui.output_plot("plotsetting") )
                              ),
                            
                            
                            ),
                 
                 
        
                
        
                
    ))
    ) #end_fluid Row
    
)
def server(input, output, session):
  
    @output
    @render.plot
    def plotsetting():
      adbg = input.adbg()
      if adbg==True:
        sns.set_style('darkgrid')
      else:
        sns.set_style('white')
      
        
    @output
    @render.plot
    def plotseasonality():
      print("plot")
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      period = input.period()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      
      dfs = df['Close'].resample('M').mean() 
      ndf = pd.DataFrame()
      ndf['Close'] = dfs
      ndf['return'] = np.log (ndf['Close']/ndf['Close'].shift(1)) * 100
      ndf['m'] = pd.DatetimeIndex(ndf.index).month
      
      if (period=='mo1'):
        ndf['mc'] = np.where(ndf['m'] != 1, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9, zorder=2.5, label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo2'):
        ndf['mc'] = np.where(ndf['m'] != 2, 0, ndf['return'])  
        bar = plt.bar(ndf.index, ndf['mc'], width=9,zorder=2.5,  label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo3'):
        ndf['mc'] = np.where(ndf['m'] != 3, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9, zorder=2.5, label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo4'):
        ndf['mc'] = np.where(ndf['m'] != 4, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9, zorder=2.5, label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo5'):
        ndf['mc'] = np.where(ndf['m'] != 5, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9,zorder=2.5,  label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo6'):
        ndf['mc'] = np.where(ndf['m'] != 6, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9, zorder=2.5, label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo7'):
        ndf['mc'] = np.where(ndf['m'] != 7, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9, zorder=2.5, label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo8'):
        ndf['mc'] = np.where(ndf['m'] != 8, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9,zorder=2.5,  label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo9'):
        ndf['mc'] = np.where(ndf['m'] != 9, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9,zorder=2.5,  label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo10'):
        ndf['mc'] = np.where(ndf['m'] != 10, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9, zorder=2.5, label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo11'):
        ndf['mc'] = np.where(ndf['m'] != 11, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9,zorder=2.5,  label='log return (mean):'+str(ndf['mc'].mean()))
      if (period=='mo12'):
        ndf['mc'] = np.where(ndf['m'] != 12, 0, ndf['return'])
        bar = plt.bar(ndf.index, ndf['mc'] ,width=9, zorder=2.5,  label='log return (mean):'+str(ndf['mc'].mean()))
        
      nr =  np.log (ndf['Close']/ndf['Close'].shift(1)) * 100
      plt.title("Seasonal data - month")
      plt.xticks(rotation=45, fontsize=9)  
      if (period =='mo0'):
        bar   =      plt.bar(ndf.index, ndf['return'], width=9,zorder=2.5, ) 
      
      i = 0
      for rect in bar:
        height = rect.get_height()
        if height != 0:
          plt.text(rect.get_x() + rect.get_width() / 2.0, nr[i], f'{nr[i]:.2f}',   ha='center', va='bottom')
        i = i+1
      plt.grid(color='grey', linestyle='-', linewidth=0.5)  
      plt.legend()
    @output
    @render.table
    def tableshift():
      stk = input.stock()
      startdate = input.start() 
      smooth = input.smoot()
      enddate = input.end()
      nday = input.nday()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      df['shf1'] = df['Close'].shift(1)
      df['shf2'] = df['Close'].shift(2)
      df['shf3'] = df['Close'].shift(3)
      df['shf_1'] = df['Close'].shift(-1)
      df['shf_2'] = df['Close'].shift(-2)
      df['shf_3'] = df['Close'].shift(-3)
      sp = []
      
      if (smooth =="sma"):
        df['sma'] = df.Close.rolling(int(nday)).mean()

      df.dropna(inplace=True)
      x,y = [],[] #support
      i =0 
      for index, r in df.iterrows():
        
        if ( r['shf_1'] >= r['Close'] and  r['shf_2'] >=  r['Close'] and r['shf_3']  >= r['Close'] and r['shf_1'] <= r['shf_2']  and r['shf_2'] <= r['shf_3'] \
        and r['shf1'] >=r['Close'] and  r['shf2'] >=r['Close']  and r['shf3'] >=r['Close']  and  r['shf1'] <=  r['shf2'] and  r['shf2'] <=  r['shf3'] ):
          #df.iloc[i]['support'] = 1
          sp.append(r['Close'])
          x = df.index[i]
          i =  i + 1
          y = r['Close']
        else:
          sp.append(10)
      df['support'] = sp    
      return df
    @output
    @render.plot
#Wrote
    def plotdiv():
      stk = input.stock()
      startdate = input.start() 
      period = input.perioddiv()
      stock=yf.Ticker(stk[0])                      # dividend data 
      
      if (period != "all"):
        #stock = stock.history(period=period)
        div  = pd.DataFrame()
        div['div'] = stock.dividends
        div['div'] = div.loc[period]
        #print(div)
      else:
        div  = pd.DataFrame()
        div['div'] = stock.dividends

      plt.bar(div.index,div['div'], width=130)
      plt.title("Mean "+str(format(div['div'].mean(),".2f"))+"%")
  
#DONE

    @output
    @render.plot
    
    def plotpchg():
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      pct_chg1 = int(input.pct_chg())
      
      nday = input.nday()
      pct_chg2 = int( input.pchg())
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      p_chg1 = df['Close'].pct_change(pct_chg1) * 100
      if pct_chg2 > 0: 
        p_chg2 = df['Close'].pct_change(pct_chg2) * 100
      
      
      plt.plot(p_chg1, label='pct-change '+str(pct_chg1))
      if pct_chg2 > 0: 
        plt.plot(p_chg2, label='pct-change '+str(pct_chg2))
      if pct_chg2 > 0: 
        plt.xlabel("mean:"+str(format(p_chg1.mean(),".5f")) +" std:"+str(pct_chg1)+":"+str(format(p_chg1.std(),".5f"))+", mean:"+str(format(p_chg2.mean(),".5f"))+" std:"+str(pct_chg2)+":"+str(format(p_chg2.std(),".5f"))  )
      else:
        plt.xlabel("mean:"+str(format(p_chg1.mean(),".5f")) +" std-"+str(pct_chg1)+":"+str(format(p_chg1.std(),".5f")))
        
      plt.title("Price Movement (ROC)")
      plt.legend(loc='upper right')
      
    @output
    @render.plot
    def plotbarpchg():
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      nday = input.nday()
      pct_chg1 = int(input.pct_chg())
      pct_chg2 = int( input.pchg())
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      p_chg1 = df['Close'].pct_change(pct_chg1) * 100
      if pct_chg2 > 0: 
        p_chg2 = df['Close'].pct_change(pct_chg2) * 100
      
      mu1 = p_chg1.mean()
      if pct_chg2 > 0: 
        mu2 = p_chg2.mean()
      
      import numpy as np
      sigma = p_chg1.std()
      n, bins, patches = plt.hist(p_chg1, 100, 
                            density = 1, 
                            color ='green',
                            alpha = 0.7)
      y1 = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
        np.exp(-0.5 * (1 / sigma * (bins - mu1))**2))
      print(p_chg1)
      if pct_chg2 > 0: 
        n, bins, patches = plt.hist(p_chg2, 100, 
                            density = 1, 
                            color ='orange',
                            alpha = 0.7)
        y2 = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
        np.exp(-0.5 * (1 / sigma * (bins - mu2))**2))
      #print(p_chg2)
      plt.plot(bins, y1, '--', color ='green', label="std"+str(pct_chg1))
      if pct_chg2 > 0: 
        plt.plot(bins, y2, '--', color ='orange', label="std"+str(pct_chg2))
      if pct_chg2 > 0: 
        plt.xlabel("mean "+str(format(p_chg1.mean(),".5f"))+", std-"+str(pct_chg1)+":"+str(format(p_chg1.std(),".5f"))+" \n"+"mean "+str(format(p_chg2.mean(),".5f"))+", std-"+str(pct_chg2)+":"+str(format(p_chg2.std(),".5f")) )
      else:
        plt.xlabel("mean "+str(format(p_chg1.mean(),".5f"))+", std-"+str(pct_chg1)+":"+str(format(p_chg1.std(),".5f")) )
      
      plt.title("Percent change ROC ")
      plt.legend(loc='upper right')
 
  
    @output
    @render.plot
    def plotsupport():
     
      stk = input.stock()
      startdate = input.start() 
  
      enddate = input.end()
      nday = input.nday()
      support = input.support()
      line1 = float(input.line1())
      line2 = float(input.line2())
      fibo1 = float(input.fibo1())
      fibo2 = float(input.fibo2())
      fibo3 = float(input.fibo3())
      fibo4 = float(input.fibo4())
      fibo5 = float(input.fibo5())
      
      resistance = input.resistance()
      
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      df['shf1'] = df['Close'].shift(1)
      df['shf2'] = df['Close'].shift(2)
      df['shf3'] = df['Close'].shift(3)
      df['shf_1'] = df['Close'].shift(-1)
      df['shf_2'] = df['Close'].shift(-2)
      df['shf_3'] = df['Close'].shift(-3)
 
      df.dropna(inplace=True)
      x,y = [],[] #support
      i =0 
      sp = []
      rs = []
      p = df.iloc[0]['Close']
      re = p
      if (line1 > 0):
        x1, y1 = [df.index[0], df.index[-1]], [line1, line1]
        plt.plot(x1, y1,  color='orange', label="support")
      if (line2 > 0):
        x2, y2 = [df.index[0], df.index[-1]], [line2, line2]
        plt.plot(x2, y2,  color='darkorange',label="resistance")
      if (line1 > 0 and line2 >0):
        if (fibo1 == True):
          point = line2 - (line2 - line1) * 0.236
          x3, y3 = [df.index[0], df.index[-1]], [point, point]
          plt.plot(x3, y3,  color='deepskyblue')
          plt.text(df.index[-1], point,"20.36%")
        if (fibo2 == True):
          point = line2 - (line2 - line1) * 0.3820
          x4, y4 = [df.index[0], df.index[-1]], [point, point]
          plt.plot(x4, y4,  color='skyblue')
          plt.text(df.index[-1], point,"38.20%")
        if (fibo3 == True):
          point = line2 - (line2 - line1) * 0.50
          x5, y5 = [df.index[0], df.index[-1]], [point, point]
          plt.plot(x5, y5,  color='lightskyblue')
          plt.text(df.index[-1], point,"50%")
        if (fibo4 == True):
          point = line2 - (line2 - line1) * 0.618
          x6, y6 = [df.index[0], df.index[-1]], [point, point]
          plt.plot(x6, y6,  color='steelblue')
          plt.text(df.index[-1], point,"61.80%")
        if (fibo5 == True):
          point = line2 - (line2 - line1) * 0.786
          x7, y7 = [df.index[0], df.index[-1]], [point, point]
          plt.plot(x7, y7,  color='royalblue')
          plt.text(df.index[-1], point,"78.60%")
      
      #define width of candlestick elements
      width = 0.9    #for drawing open to close price
      width2 = 0.09  #for drawing high/low price

#define up and down prices
      up = df[df.Close>=df.Open]
      down = df[df.Close<df.Open]
#define colors to use
      col1 = 'green'
      col2 = 'red'
      #plot up prices
      plt.bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=col1)
      #draw high-price line
      plt.bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=col1)
      #draw low-price line
      plt.bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=col1)
      #plot down prices
      plt.bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=col2)
      plt.bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=col2)
      plt.bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=col2)
       
      #rotate x-axis tick labels
    
      plt.xticks(rotation=45, ha='right')
     

      if (support == True or resistance == True):  
        for index, r in df.iterrows():
          if ( r['shf_1'] >= r['Close'] and  r['shf_2'] >=  r['Close'] and r['shf_3']  >= r['Close'] and r['shf_1'] <= r['shf_2']  and r['shf_2'] <= r['shf_3'] \
          and r['shf1'] >=r['Close'] and  r['shf2'] >=r['Close']  and r['shf3'] >=r['Close']  and  r['shf1'] <=  r['shf2'] and  r['shf2'] <=  r['shf3'] ):
            #df.iloc[i]['support'] = 1
            sp.append(r['Close'])
            p = r['Close']
          else:
            sp.append(p)
          if ( r['shf_1'] <= r['Close'] and  r['shf_2'] <=  r['Close'] and r['shf_3']  <= r['Close'] and r['shf_1'] >= r['shf_2']  and r['shf_2'] >= r['shf_3'] \
          and r['shf1'] <=r['Close'] and  r['shf2'] <=r['Close']  and r['shf3'] <=r['Close']  and  r['shf1'] >=  r['shf2'] and  r['shf2'] >=  r['shf3'] ):
            rs.append(r['Close'])
            re = r['Close']
          else:
            rs.append(re)
             
        df['support'] = sp
        df['resistance'] = rs
      if (support == True):
        plt.plot(df['support'], label="sug. support", color='green')
        plt.legend()
      if (resistance == True):
        plt.plot(df['resistance'], label="sug. resistance",color='red')
        plt.legend(loc="upper right")

    @output
    @render.plot
    def plotmeanrev():
      stk = input.stock()
      startdate = input.start() 
      ema = input.revema()
      sma = input.revsma()
      enddate = input.end()
      data = yf.download(stk[0], start=startdate, end=enddate)

      data['ema'] = data['Close'].ewm(com=1.5,min_periods=int(ema)).mean()
      data['sma'] = data['Close'].rolling(int(sma)).mean()
      #data['rev'] = data.loc[data['sma'] > data['e/ma'],data['ema'] ]
      data["rev"] = data["sma"] + 3
      data.loc[data["sma"] > data["ema"], "rev"] = data["ema"] - 3
      #print(data)
      data.dropna(inplace=True)
#      data['rev'] = dataf['Discount'].apply(lambda x : 20 if x > 20 else x)
      plt.plot(data['Close'],label='Close')
      plt.plot(data['sma'],label='ema-'+str(ema))
      plt.plot(data['ema'],label='sma-'+str(sma))
      plt.plot(data['rev'],label='rev-')
      import matplotlib.pyplot
      bottom, top = plt.gca().get_ylim()

      plt.legend()
    @output
    @render.plot
    def plotcycle1m():
      stk = input.stock()
      df,ind = plotstockall(stk[0], period="1mo")
      typecy = input.typecy()
      if (typecy =='close'):
        plt.plot(df['Close'], label=ind, color='blue')
        
      if (typecy =='return'):
        df['return'] =  (df['Close'] - df['Close'].shift(1) )/ df['Close'] * 100
        df['creturn'] = df['return'].cumsum()
        cpct = str(df['creturn'].iloc[-1])
        plt.xlabel('Return '+cpct)
        plt.plot(df['creturn'], color='orange',label='Return')
        
      if (typecy =='pctchg'):
        df['pct'] = df['Close'].pct_change(1)
        df['cpct'] = df['pct'].cumsum()
        cpct = str(df['cpct'].iloc[-1])
        plt.xlabel('Pct-chg '+cpct)
        plt.plot(df['pct'], color='orange', label='Pct-chg')
        
      plt.title(stk[0]+" - cycle 1M ")
      
    
      plt.legend(loc='upper right') 
      plt.xticks([])
 
    @output
    @render.plot
    def plotmean():
      stk = input.stock()
      df,ind = plotstockall(stk[0], period="1mo")
      plt.title(stk[0]+" - cycle 1M")
      plt.plot(df['Close'], label=ind)
      plt.legend(loc='upper right') 
      plt.xticks([])
      return
    @output
    @render.plot
    def plotcycle2m():
      stk = input.stock()
      df,ind = plotstockall(stk[0], period="2mo")
      typecy = input.typecy()
      if (typecy =='close'):
        plt.plot(df['Close'], label=ind, color='blue')
        
      if (typecy =='return'):
        df['return'] =  (df['Close'] - df['Close'].shift(1) )/ df['Close'] * 100
        df['creturn'] = df['return'].cumsum()
        cpct = str(df['creturn'].iloc[-1])
        plt.xlabel('Return '+cpct)
        plt.plot(df['creturn'], color='orange',label='Return')
        
      if (typecy =='pctchg'):
        df['pct'] = df['Close'].pct_change(1)
        df['cpct'] = df['pct'].cumsum()
        cpct = str(df['cpct'].iloc[-1])
        plt.xlabel('Pct-chg '+cpct)
        plt.plot(df['pct'], color='orange', label='Pct-chg')
        
      plt.title(stk[0]+" - cycle 2M ")
      
    
      plt.legend(loc='upper right') 
      plt.xticks([])
 
    @output
    @render.plot
    def plotcycle3m():
      stk = input.stock()
      df,ind = plotstockall(stk[0], period="3mo")
      typecy = input.typecy()
      if (typecy =='close'):
        plt.plot(df['Close'], label=ind, color='blue')
        
      if (typecy =='return'):
        df['return'] =  (df['Close'] - df['Close'].shift(1) )/ df['Close'] * 100
        df['creturn'] = df['return'].cumsum()
        cpct = str(df['creturn'].iloc[-1])
        plt.xlabel('Return '+cpct)
        plt.plot(df['creturn'], color='orange',label='Return')
        
      if (typecy =='pctchg'):
        df['pct'] = df['Close'].pct_change(1)
        df['cpct'] = df['pct'].cumsum()
        cpct = str(df['cpct'].iloc[-1])
        plt.xlabel('Pct-chg '+cpct)
        plt.plot(df['pct'], color='orange', label='Pct-chg')
        
      plt.title(stk[0]+" - cycle 3M ")
      
    
      plt.legend(loc='upper right') 
      plt.xticks([])
 
    @output
    @render.plot
    def plotcycle4m():
      stk = input.stock()
      df,ind = plotstockall(stk[0], period="4mo")
      typecy = input.typecy()
      if (typecy =='close'):
        plt.plot(df['Close'], label=ind, color='blue')
        
      if (typecy =='return'):
        df['return'] =  (df['Close'] - df['Close'].shift(1) )/ df['Close'] * 100
        df['creturn'] = df['return'].cumsum()
        cpct = str(df['creturn'].iloc[-1])
        plt.xlabel('Return '+cpct)
        plt.plot(df['creturn'], color='orange',label='Return')
        
      if (typecy =='pctchg'):
        df['pct'] = df['Close'].pct_change(1)
        df['cpct'] = df['pct'].cumsum()
        cpct = str(df['cpct'].iloc[-1])
        plt.xlabel('Pct-chg '+cpct)
        plt.plot(df['pct'], color='orange', label='Pct-chg')
        
      plt.title(stk[0]+" - cycle 4M ")
      
    
      plt.legend(loc='upper right') 
      plt.xticks([])
 
    @output
    @render.plot
    def plotcycle5m():
      stk = input.stock()
      df,ind = plotstockall(stk[0], period="5mo")
      typecy = input.typecy()
      if (typecy =='close'):
        plt.plot(df['Close'], label=ind, color='blue')
        
      if (typecy =='return'):
        df['return'] =  (df['Close'] - df['Close'].shift(1) )/ df['Close'] * 100
        df['creturn'] = df['return'].cumsum()
        cpct = str(df['creturn'].iloc[-1])
        plt.xlabel('Return '+cpct)
        plt.plot(df['creturn'], color='orange',label='Return')
        
      if (typecy =='pctchg'):
        df['pct'] = df['Close'].pct_change(1)
        df['cpct'] = df['pct'].cumsum()
        cpct = str(df['cpct'].iloc[-1])
        plt.xlabel('Pct-chg '+cpct)
        plt.plot(df['pct'], color='orange', label='Pct-chg')
        
      plt.title(stk[0]+" - cycle 5M ")
      
    
      plt.legend(loc='upper right') 
      plt.xticks([])
 
    @output
    @render.plot
    def plotcycle6m():
      stk = input.stock()
      df,ind = plotstockall(stk[0], period="6mo")
      typecy = input.typecy()
      if (typecy =='close'):
        plt.plot(df['Close'], label=ind, color='blue')
        
      if (typecy =='return'):
        df['return'] =  (df['Close'] - df['Close'].shift(1) )/ df['Close'] * 100
        df['creturn'] = df['return'].cumsum()
        cpct = str(df['creturn'].iloc[-1])
        plt.xlabel('Return '+cpct)
        plt.plot(df['creturn'], color='orange',label='Return')
        
      if (typecy =='pctchg'):
        df['pct'] = df['Close'].pct_change(1)
        df['cpct'] = df['pct'].cumsum()
        cpct = str(df['cpct'].iloc[-1])
        plt.xlabel('Pct-chg '+cpct)
        plt.plot(df['pct'], color='orange', label='Pct-chg')
        
      plt.title(stk[0]+" - cycle 6M ")
      
    
      plt.legend(loc='upper right') 
      plt.xticks([])
 
    @output
    @render.plot
    def plotcycle1y():
      stk = input.stock()
      df,ind = plotstockall(stk[0], period="1y")
      typecy = input.typecy()
      if (typecy =='close'):
        plt.plot(df['Close'], label=ind, color='blue')
        
      if (typecy =='return'):
        df['return'] =  (df['Close'] - df['Close'].shift(1))/ df['Close'] * 100
        df['creturn'] = df['return'].cumsum()
        cpct = str(df['creturn'].iloc[-1])
        plt.xlabel('Return '+cpct)
        plt.plot(df['creturn'], color='orange',label='Return')
        
      if (typecy =='pctchg'):
        df['pct'] = df['Close'].pct_change(1)
        df['cpct'] = df['pct'].cumsum()
        cpct = str(df['cpct'].iloc[-1])
        plt.xlabel('Pct-chg '+cpct)
        plt.plot(df['pct'], color='orange', label='Pct-chg')
        
      plt.title(stk[0]+" - cycle 1Y ")
      
    
      plt.legend(loc='upper right') 
      plt.xticks([])
 
    @output
    @render.plot
    def plotcycle2y():
      stk = input.stock()
      df,ind = plotstockall(stk[0], period="2y")
      typecy = input.typecy()
      if (typecy =='close'):
        plt.plot(df['Close'], label=ind, color='blue')
        
      if (typecy =='return'):
        df['return'] =  (df['Close'] - df['Close'].shift(1) )/ df['Close'] * 100
        df['creturn'] = df['return'].cumsum()
        cpct = str(df['creturn'].iloc[-1])
        plt.xlabel('Return '+cpct)
        plt.plot(df['creturn'], color='orange',label='Return')
        
      if (typecy =='pctchg'):
        df['pct'] = df['Close'].pct_change(1)
        df['cpct'] = df['pct'].cumsum()
        cpct = str(df['cpct'].iloc[-1])
        plt.xlabel('Pct-chg '+cpct)
        plt.plot(df['pct'], color='orange', label='Pct-chg')
        
      plt.title(stk[0]+" - cycle 2Y ")
      
    
      plt.legend(loc='upper right') 
      plt.xticks([])
 
    @output
    @render.plot
    def plotcycle3y():
      stk = input.stock()
      df,ind = plotstockall(stk[0], period="3y")
      typecy = input.typecy()
      if (typecy =='close'):
        plt.plot(df['Close'], label=ind, color='blue')
        
      if (typecy =='return'):
        df['return'] =  (df['Close'] - df['Close'].shift(1) )/ df['Close'] * 100
        df['creturn'] = df['return'].cumsum()
        cpct = str(df['creturn'].iloc[-1])
        plt.xlabel('Return '+cpct)
        plt.plot(df['creturn'], color='orange',label='Return')
        
      if (typecy =='pctchg'):
        df['pct'] = df['Close'].pct_change(1)
        df['cpct'] = df['pct'].cumsum()
        cpct = str(df['cpct'].iloc[-1])
        plt.xlabel('Pct-chg '+cpct)
        plt.plot(df['pct'], color='orange', label='Pct-chg')
        
      plt.title(stk[0]+" - cycle 3Y ")
      
    
      plt.legend(loc='upper right') 
      plt.xticks([])
 
    def plotstockall(stock, period=""):
      startdate = input.start() 
      enddate = input.end()
     
      nday = input.nday()
      if period=="":
        df = yf.download(stock,startdate, enddate, auto_adjust=True)
        
      else:
        df = yf.Ticker(stock)
        df = df.history(period=period)

      if df['Close'].iloc[-1] > df['Close'].iloc[0]:
        ind = "Up"
      elif df['Close'].iloc[-1] < df['Close'].iloc[0]:
        ind = "Down"
      else:
        ind = "Unchange"
      return [df,ind]
    #DONE
    @output
    @render.plot
    def plotscatter():
      stk = input.stock()
      scatter = input.scatter()
      if len(stk) > 1:
        stk = " ".join(stk)
      else:
        stk = stk[0]
      startdate = input.start() 
      enddate = input.end()
      pct_chg = int(input.pct_chg())
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      if (len(stk) > 7 ):    
        stk = stk.split(" ") #Get list symbol
        datal = pd.DataFrame()
        for i in stk:
          if scatter =='pct': #percent change
            datal[i] = df['Close'][i].pct_change(pct_chg) * 100
            plt.scatter(datal[i].index,datal[i],s=4,label=i)
            plt.title("Pct-chg: "+str(pct_chg)+' day')
          else:
            datal[i] = df['Volume'][i]
            plt.scatter(datal[i].index,datal[i],s=4,label=i)
            plt.title("Volume ")
      else:
          if scatter =='pct':
            datal = df['Close'].pct_change(pct_chg) * 100
            plt.scatter(datal.index,datal,s=4,label=stk)
            plt.title("Pct-chg: "+str(pct_chg)+' day')

          else:  
            datal = df['Volume']
            plt.scatter(datal.index,datal,s=4,label=stk)
            plt.title("Volume ")

      plt.legend(loc='upper right')

    @output
    @render.plot
    def plotshift():
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      shf = int(input.shf())
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      
      datal = pd.DataFrame()
      #scatter shift for the first stock only
      datal['shift'] = df['Close'].shift(shf)
      datal['Close'] = df['Close']
      
      #datal = datal.fillna(0)
      datal = datal.dropna()
      #plt.plot(datal.index, datal, marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
      #plt.plot(df['Close'].index,df['Close'], marker="o", markersize=20, markeredgecolor="red", markerfacecolor="green")
      df.dropna()
      fig, ax = plt.subplots()
      fig.set_figheight(15)
      fig.set_figwidth(25)
      plt.title("Shift: "+str(shf)+" day")
      plt.legend(loc='upper right')
      ax,scatter(datal.index,datal['shift'],s=4,label='shift')
      #plt.scatter(datal.index,datal['shift'],s=4,label='shift')
      ax.scatter(datal['Close'].index,datal['Close'],s=4,label='close')

      #plt.scatter(datal['Close'].index,datal['Close'],s=4,label='close')

    @output
    @render.plot
    def plotstock():
      #print(plt.style.available)
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      line = input.line()
      sma = input.sma()
      ema = input.ema()
      mo = input.mo()
      nday = input.nday()
      
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      p = df['Close'] 
      fig, ax = plt.subplots()
      fig.set_figheight(15)
      fig.set_figwidth(25)
      
      if (line == True):
        #data = yf.download(stock, start="2022-01-01", end="2023-12-28")
        ax.plot( df.index, df['Close'], label='Price', color='green')

        ax.set(xlabel='Year', ylabel='Price',
           title=stk)
        ax.grid()

          #plt.plot(df['Close'], label='close', color='blue')
      
      if (sma == True):
          sma = df['Close'].rolling(int(nday)).mean()
          plt.plot(sma, label='sma', color='red')
          plt.plot(df['Close'], label='close', color='blue')
      
      if (mo == True):
          mo =  df['Close'] - df['Close'].shift(int(nday))
          
          plt.plot(mo, label='mo')
      if (ema==True):
          ema = df['Close'].ewm(com=1.5,min_periods=int(nday)).mean()
          plt.plot(ema, label='ema', color='green')
          plt.plot(df['Close'], label='close', color='blue')
      
      #plt.title("Price")
      #plt.legend(loc='upper right')
   
    #DONE
    @output
    @render.plot
    def plotstockmacd():
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      emafast = int(input.emafast())
      emaslow = int(input.emaslow())
      sig = emaslow - emafast
      tplot = input.tplot()
     
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      df['ema12'] = ta.ema(df['Close'],length=emafast)
      df['ema26'] = ta.ema(df['Close'],length=emaslow)
      
      df['macd'] =  df['ema12'] -  df['ema26']
      df['signal'] = ta.ema(df['macd'], length = sig)
      
      fig, ax = plt.subplots(2,1, figsize=(400, 250))
      
      if tplot == "candle":
        width = 0.9    #for drawing open to close price
        width2 = 0.09  #for drawing high/low price

#define up and down prices
        up = df[df.Close>=df.Open]
        down = df[df.Close<df.Open]
#define colors to use
        col1 = 'green'
        col2 = 'red'
      
          
      #plot up prices
        ax[0].bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=col1)
        #draw high-price line
        ax[0].bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=col1)
        #draw low-price line
        ax[0].bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=col1)
        #plot down prices
        ax[0].bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=col2)
        ax[0].bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=col2)
        ax[0].bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=col2)
        #rotate x-axis tick labels
        plt.xticks(rotation=45, ha='right')
      else:
        ax[0].plot(df['Close'], color='blue', label='close')
        
      ax[0].plot(df['ema12'], color='green', label='ema-12')
      ax[0].plot(df['ema26'], color='red',label='ema-26')
      ax[0].legend()
        #plt.subplots(2,1,2,figsize=(300, 150))
      ax[1].plot(df['macd'],  color='red', label='macd')
      ax[1].plot(df['signal'], color='green',label='signal')
      ax[1].legend()
      
#DONE
    @output
    @render.plot
    def plothistory():
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      
      plt.title("Price/year")
      #plt.plot(df['Adj Close'], label='close')
      df['Date'] = pd.to_datetime(df.index)
      #plt.plot()
      sns.lineplot(x=df['Date'].dt.dayofyear, 
             y=df['Close'], 
             hue=df['Date'].dt.year);
      plt.legend(loc='upper right')
#DONE
    @output
    @render.plot
    @reactive.event(input.goboll, ignore_none=True)
    def plotbollinger():
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      nday = input.nday()
      data = yf.download(stk,startdate, enddate, auto_adjust=True)
      TP = (data['High']+data['Low']+data['Close'])/3
      n = int(nday)
      sigma = TP.rolling(n, min_periods=n).std() 
      m = 2
      UBB = TP.rolling(window=n).mean() + m * sigma
      LBB = TP.rolling(window=n).mean() - m * sigma

#Plot handle stick….

      plt.plot(UBB, label='upper')
      plt.plot(data['Close'].index,data['Close'], label="close")
      plt.plot(LBB,label='lower')
      plt.legend(loc="upper right")
    @output
    @render.plot
    @reactive.event(input.gov, ignore_none=True)
    def plotcycle1yv():
      stk = input.stock()
      nday = int(input.nday())
      showreturn = input.showreturn()  
      showvu = input.showvu()
      showvd = input.showvd()

      df,ind = plotstockall(stk[0], period="1y")
      df['return'] =  (df['Close']/df['Close'].shift(1) - 1   ) * 100
      df['volatile'] =  df['return'].rolling(nday).std() * np.sqrt(nday)
      df.dropna(inplace=True)
      sd = df['return'].std()
      plt.plot(df['Close'].index, df['Close'], label="Close ")
      if (showreturn == True):
        plt.plot(df['return'].index, df['return'], label="return ")
      if (showvu == True):
        df['v'] = df['Close'].rolling(nday).mean() +  sd 
        plt.plot(df['v'].index, df['v'], label="Volatile price")
      if (showvd == True):
        df['vn'] = df['Close'].rolling(nday).mean() - sd
        plt.plot(df['vn'].index, df['vn'], label="Volatile price")
      plt.title('Volatility: 1Y, SD:' + str(sd))
      plt.legend(loc='upper right') 
      plt.xticks([])
 
    @output
    @render.plot
    @reactive.event(input.gov, ignore_none=True)
    def plotcycle2yv():
      stk = input.stock()
      nday = int(input.nday())
      showreturn = input.showreturn() 
      showvu = input.showvu()
      showvd = input.showvd()

      df,ind = plotstockall(stk[0], period="2y")
      df['return'] =  (df['Close']/df['Close'].shift(1) - 1   ) * 100
      df['volatile'] =  df['return'].rolling(nday).std() * np.sqrt(nday)
  
      df.dropna(inplace=True)
      sd = df['return'].std()
      plt.plot(df['Close'].index, df['Close'], label="Close ")
      if (showreturn == True):
        plt.plot(df['return'].index, df['return'], label="return ")
      if (showvu == True):
        df['v'] = df['Close'].rolling(nday).mean() +  sd 
        plt.plot(df['v'].index, df['v'], label="Volatile price")
      if (showvd == True):
        df['vn'] = df['Close'].rolling(nday).mean() - sd
        plt.plot(df['vn'].index, df['vn'], label="Volatile price")
      plt.title('Volatility: 2Y, SD:' + str(sd))
      plt.legend(loc='upper right') 
      plt.xticks([])      
      
    @output
    @render.plot
    @reactive.event(input.gov, ignore_none=True)
    def plotcycle3yv():
      stk = input.stock()
      showreturn = input.showreturn()     
      showvu = input.showvu()
      showvd = input.showvd()

      nday = int(input.nday())
      df,ind = plotstockall(stk[0], period="3y")
      df['return'] =  (df['Close']/df['Close'].shift(1) - 1   ) * 100
      df['volatile'] =  df['return'].rolling(nday).std() * np.sqrt(nday)
      
      df.dropna(inplace=True)
      sd = df['return'].std()
      plt.plot(df['Close'].index, df['Close'], label="Close ")
      if (showreturn == True):
        plt.plot(df['return'].index, df['return'], label="return ")
      if (showvu == True):
        df['v'] = df['Close'].rolling(nday).mean() +  sd 
        plt.plot(df['v'].index, df['v'], label="Volatile price")
      if (showvd == True):
        df['vn'] = df['Close'].rolling(nday).mean() - sd
        plt.plot(df['vn'].index, df['vn'], label="Volatile price")
      plt.title('Volatility: 3Y, SD:' + str(sd))
      plt.legend(loc='upper right') 
      plt.xticks([])
    @output
    @render.plot
    @reactive.event(input.gov, ignore_none=True)
    def plotcycle4mv():
      stk = input.stock()
      nday = int(input.nday())
      showreturn = input.showreturn()  
      showvu = input.showvu()
      showvd = input.showvd()

      df,ind = plotstockall(stk[0], period="4mo")
      df['return'] =  (df['Close']/df['Close'].shift(1) - 1   ) * 100
      df['volatile'] =  df['return'].rolling(nday).std() * np.sqrt(nday)
      df.dropna(inplace=True)
      plt.plot(df['Close'].index, df['Close'], label="Close ")
      sd = df['return'].std()
      if (showreturn == True):
        plt.plot(df['return'].index, df['return'], label="return ")
      if (showvu == True):
        df['v'] = df['Close'].rolling(nday).mean() +  sd 
        plt.plot(df['v'].index, df['v'], label="Volatile price")
      if (showvd == True):
        df['vn'] = df['Close'].rolling(nday).mean() - sd
        plt.plot(df['vn'].index, df['vn'], label="Volatile price")
      plt.title('Volatility: 4M, SD:' + str(sd))
      plt.legend(loc='upper right') 
      plt.xticks([])
    @output
    @render.plot
    @reactive.event(input.gov, ignore_none=True)
    def plotcycle5mv():
      stk = input.stock()
      nday = int(input.nday())
      showreturn = input.showreturn()  
      showvu = input.showvu()
      showvd = input.showvd()

      df,ind = plotstockall(stk[0], period="5mo")
      df['return'] =  (df['Close']/df['Close'].shift(1) - 1   ) * 100
      df['volatile'] =  df['return'].rolling(nday).std() * np.sqrt(nday)
      df.dropna(inplace=True)
      plt.plot(df['Close'].index, df['Close'], label="Close ")
      sd = df['return'].std()
      if (showreturn == True):
        plt.plot(df['return'].index, df['return'], label="return ")
      if (showvu == True):
        df['v'] = df['Close'].rolling(nday).mean() +  sd 
        plt.plot(df['v'].index, df['v'], label="Volatile price")
      if (showvd == True):
        df['vn'] = df['Close'].rolling(nday).mean() - sd
        plt.plot(df['vn'].index, df['vn'], label="Volatile price")
      plt.title('Volatility: 5M, SD:' + str(sd))
      plt.legend(loc='upper right') 
      plt.xticks([])
    @output
    @render.plot
    @reactive.event(input.gov, ignore_none=True)
    def plotcycle6mv():
      stk = input.stock()
      nday = int(input.nday())
      showreturn = input.showreturn()
      showvu = input.showvu()
      showvd = input.showvd()

      df,ind = plotstockall(stk[0], period="6mo")
      df['return'] =  (df['Close']/df['Close'].shift(1) - 1   ) * 100
      plt.plot(df['Close'].index, df['Close'], label="Close ")
      df.dropna(inplace=True)
      sd = df['return'].std()
      if (showreturn == True):
        plt.plot(df['return'].index, df['return'], label="return ")
      if (showvu == True):
        df['v'] = df['Close'].rolling(nday).mean() +  sd 
        plt.plot(df['v'].index, df['v'], label="Volatile price")
      if (showvd == True):
        df['vn'] = df['Close'].rolling(nday).mean() - sd
        plt.plot(df['vn'].index, df['vn'], label="Volatile price")
      plt.title('Volatility: 6M, SD:' + str(sd))
      plt.legend(loc='upper right') 
      plt.xticks([])
    @output
    @render.plot
    @reactive.event(input.gov, ignore_none=True)
    def plotcycle1mv():
      stk = input.stock()
      nday = int(input.nday())
      showvu = input.showvu()
      showvd = input.showvd()

      showreturn = input.showreturn()
      df,ind = plotstockall(stk[0], period="1mo")
      df['return'] =  (df['Close']/df['Close'].shift(1) - 1   ) * 100
      df['volatile'] =  df['return'].rolling(nday).std() * np.sqrt(nday)
      df.dropna(inplace=True)
      sd = df['return'].std()
      plt.plot(df['Close'].index, df['Close'], label="Close ")
      if (showreturn == True):
        plt.plot(df['return'].index, df['return'], label="return ")
      if (showvu == True):
        df['v'] = df['Close'].rolling(nday).mean() +  sd 
        plt.plot(df['v'].index, df['v'], label="Volatile price")
      if (showvd == True):
        df['vn'] = df['Close'].rolling(nday).mean() - sd
        plt.plot(df['vn'].index, df['vn'], label="Volatile price")
      plt.title('Volatility: 1M, SD:' + str(sd))
      plt.legend(loc='upper right') 
      plt.xticks([])
    
    @output
    @render.plot
    @reactive.event(input.gov, ignore_none=True)
    def plotcycle2mv():
      stk = input.stock()
      nday = int(input.nday())
      showreturn = input.showreturn()      
      df,ind = plotstockall(stk[0], period="2mo")
      df['return'] =  (df['Close']/df['Close'].shift(1) - 1   ) * 100
      df['sma'] =  df['Close'].rolling(nday).mean() 
      df['volatile'] =  df['return'].rolling(nday).std() * np.sqrt(nday)
      showvu = input.showvu()
      showvd = input.showvd()
      
      sd = df['return'].std() 
      sdsma = df['sma'].std() 
      df.dropna(inplace=True)
      plt.plot(df['Close'].index, df['Close'], label="Close ")
      if (showreturn == True):
        plt.plot(df['return'].index, df['return'], label="return ")
      if (showvu == True):
        df['v'] = df['Close'].rolling(nday).mean() +  sd 
        plt.plot(df['v'].index, df['v'], label="Volatile price")
      if (showvd == True):
        df['vn'] = df['Close'].rolling(nday).mean() - sd
        plt.plot(df['vn'].index, df['vn'], label="Volatile price")
      plt.title('Implied volatility: 2M')
      plt.title("Volatility: 2M, , SD:" + str(sd))
      plt.legend(loc='upper right') 
      plt.xticks([])
    
    @output
    @render.plot
    @reactive.event(input.gov, ignore_none=True)
    def plotcycle3mv():
      stk = input.stock()
      nday = int(input.nday())
      showreturn = input.showreturn()
      df,ind = plotstockall(stk[0], period="3mo")
      df['return'] =  (df['Close']/df['Close'].shift(1) - 1   ) * 100
      df['sma'] =  df['Close'].rolling(nday).mean() 
      df['volatile'] =  df['return'].rolling(nday).std() #* np.sqrt(nday)
      sd = df['return'].std()
      showvu = input.showvu()
      showvd = input.showvd()
      sd = df['return'].std()
      df.dropna(inplace=True)
      plt.plot(df['Close'].index, df['Close'], label="Close ")
      if (showreturn == True):
        plt.plot(df['return'].index, df['return'], label="return ")
      if (showvu == True):
        df['v'] = df['Close'].rolling(nday).mean() +  sd 
        plt.plot(df['v'].index, df['v'], label="Volatile price")
      if (showvd == True):
        df['vn'] = df['Close'].rolling(nday).mean() - sd
        plt.plot(df['vn'].index, df['vn'], label="Volatile price")
      plt.title('Implied volatility: 3M, SD:' + str(sd))
      plt.title("Volatility: 3M, SD:" + str(sd))
      plt.legend(loc='upper right') 
      plt.xticks([])
        
    @output
    @render.plot
    def plotsdvolatile():
      print("Plot volatile")
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      nday = int(input.nday())
      show30 = input.show30()
      show60 = input.show60()
      showclose = input.showclose()
      showreturn = input.showreturn()
      showlog = input.showlog()
      showvu = input.showvu()
      showvd = input.showvd()
      
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      df['return'] =  (df['Close']/df['Close'].shift(1) - 1   ) *100
      df['volatile'] =  df['return'].rolling(nday).std() 
      sd = df['return'].std()
     
      
      if (show30 == True):
        df['volatile30'] =  df['return'].rolling(30).std() #* np.sqrt(250)
      if (show60 == True):
        df['volatile60'] =  df['return'].rolling(60).std() #* np.sqrt(250)
      df.dropna(inplace=True)

      if (showreturn == True):
        plt.plot(df['return'].index, df['return'], label="return ")
      if (show30 == True):
        plt.plot(df['volatile30'].index, df['volatile30'], label="volatility-30")
      if (show60 == True):
        plt.plot(df['volatile60'].index, df['volatile60'], label="volatility-60")
      if (showclose == True):
        plt.plot(df['Close'].index, df['Close'], label="close ")
      if (showlog == True):
        plt.plot(df['return'].index, df['return'].cumsum(), label="cum-return")
      if (showvu == True):
        df['v'] = df['Close'].rolling(nday).mean() +  sd 
        plt.plot(df['v'].index, df['v'], label="Volatile price")
      if (showvd == True):
        df['vn'] = df['Close'].rolling(nday).mean() - sd
        plt.plot(df['vn'].index, df['vn'], label="Volatile price")

      plt.plot(df['volatile'].index, df['volatile'], label="volatility-"+str(nday))
      plt.title('Historical volatility:'+str(startdate)+" to "+str(enddate)+" sd:"+str(format(sd,".5f")))
      plt.legend(loc='upper right')
    @output
    @render.plot
    def normalizedplot():  #Growth
      #plt.style.use('seaborn-darkgrid')
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      ndf = df['Close']/ df['Close'].iloc[0] * 100 
      
      plt.title("Growth Rate % ")
      plt.plot(ndf,label=stk)
      plt.legend(loc='upper right')
      #plt.bar(2022, 100, 100, 0)
      
    #PORT Decision Making  
    @output
    @render.plot
    def plotportreturn():  #Growth
      #plt.style.use('seaborn-darkgrid')
      stk = input.stock()
      ratio = input.ratio()
      ratio = ratio.split(' ')
      print(ratio)
      startdate = input.start() 
      enddate = input.end()
      #plt.title("Return : cumulative return  "+str(df['cumsum'].iloc[-1]))
      ld = []
      #c = []
      
      for i in stk:
        df = yf.download(i,startdate, enddate, auto_adjust=True)
        df['cum'] =( df['Close'] - df['Close'].shift(1) )/df['Close'].shift(1) * 100
        df['c'] = df['cum'].cumsum()
        ld.append(round(df['c'].iloc[-1],4))
        #c.append(df['Close'].iloc[-1])
        plt.plot(df['cum'].cumsum(),label=i+".return:"+str(round(df['c'].iloc[-1],4)))
      
      
      if (len(ld)== len(ratio)):
        total = 0
        for i in range(len(ratio)):
          total = total +  int(ratio[i])/100 * ld[i] 
        plt.title("Port return:"+str(total))  
      else:
        plt.title("Port return")  
      plt.legend(loc='upper right')
    #DONE
    @output
    @render.plot
    def plotreturn():  #Growth
      #plt.style.use('seaborn-darkgrid')
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      logreturn = input.logreturn()
      sdreturn = input.sdreturn()
      nday = int(input.nday())
      cumsum = input.cumsum()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      df['return'] =( df['Close'] - df['Close'].shift(1) )/df['Close'].shift(1) * 100
      df['cumsum'] = df['return'].cumsum()
      sd = df['return'].rolling(nday).mean().std()
      
      if logreturn ==True:
        import numpy as np
        df['log'] = np.log (df['Close']/df['Close'].iloc[0]) * 100
        plt.plot(df['log'],label="Log return")
        plt.title("Last day log return  "+str(format(df['log'].iloc[-1],".5f")))
    
      if sdreturn ==True:
        sd = df['Close'].rolling(nday).mean().std()
        df['volatile'] = df['return'].rolling(nday).mean()
      if cumsum ==True:
        plt.plot(df['cumsum'],label="Cumulative return")

      if sdreturn ==True:
        plt.plot(df['volatile'],label="Volatile")
      if logreturn ==False:
        plt.plot(df['return'],label="Return")
        plt.title("Cumulative return  "+str(format(df['cumsum'].iloc[-1],".5f"))+" SD:"+str(format(sd, ".5f")))
      plt.legend(loc='upper right')
    
  
    @output
    @render.plot
    def plotreturnhis():  
      #plt.style.use('seaborn-darkgrid')
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      rper = input.rper()
      df = yf.Ticker(stk[0])
      df = df.history(period=rper)
        
#      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      ndf =(df['Close'] - df['Close'].shift(1) )/df['Close'].shift(1) * 100
      #ndf= df['Close'].pct_change(1) * 100
      print(df.shape)
      print(ndf.shape)
      mu = ndf.mean()
      import numpy as np
      sigma = ndf.std()
      n, bins, patches = plt.hist(ndf, 100, 
                            density = 1, 
                            color ='green',
                            alpha = 0.7)
  
      y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
        np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
 
      plt.plot(bins, y, '--', color ='black', label="std")
      plt.xlabel("mean: "+str(format(mu,".5f"))+", std:"+str(format(sigma,".5f")))
      plt.title("Return " + str(format(ndf.cumsum().iloc[-1],".5f")))
      plt.legend(loc='upper right')
  

              
    @output
    @render.plot
    def plotreturnperiod():  #Growth
      #plt.style.use('seaborn-darkgrid')
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      rper = input.rper()
      #df = yf.download(stk,startdate, enddate, auto_adjust=True)
      df = yf.Ticker(stk[0])
      df = df.history(period=rper)

      ndf =( df['Close'] - df['Close'].shift(1) )/df['Close'].shift(1) * 100
      df['cumsum'] = ndf.cumsum()
      plt.title("Return : cumulative return  "+str(df['cumsum'].iloc[-1]))
      #h = plt.subplot(1,1,1)
      #h1 = h.twinx()
      
      #h.plot(df['Close'],label="Return")
      plt.plot(ndf.cumsum(),label="Cumulative return", color='blue')
      
      plt.legend(loc='upper right')
      
    
    
    @output
    @render.plot
    def plotsampling():
      #plt.style.use('seaborn-darkgrid')
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      timef = input.timef()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      index = pd.date_range(startdate, enddate, freq=timef)
      
      plt.title("Price in Time Frame")
#define width of candlestick elements
      width = 0.9    #for drawing open to close price
      width2 = 0.09  #for drawing high/low price

#define up and down prices
      up = df[df.Close>=df.Open]
      down = df[df.Close<df.Open]
#define colors to use
      col1 = 'green'
      col2 = 'red'
      #plt.grid(axis='both')

      #plot up prices
      plt.bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=col1)
      #draw high-price line
      plt.bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=col1)
      #draw low-price line
      plt.bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=col1)
      
      #plot down prices
      plt.bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=col2)
      plt.bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=col2)
      plt.bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=col2)
      plt.tick_params(axis="both", direction="in", pad=5)
      #rotate x-axis tick labels
      plt.xticks(rotation=45, ha='right')
      import matplotlib.pyplot
      bottom, top = plt.gca().get_ylim()
  
      plt.vlines(index, ymin=bottom.min(),ymax=top,  color="black",linestyle='dotted')      

    
    def plotreturnstock():
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      df['lag'] = df.Close.shift(1)
      df['return'] = df.Close / df['lag'] - 1
      plt.title("Return ")
      plt.plot(df['return'])
    @output
    @render.plot
    def candleplot():
      stk = input.stock()
      startdate = input.start()
      enddate = input.end()
      cansma = input.cansma()
      canema = input.canema()
      canb = input.canb()
      strong = input.strong()
      nday = input.nday()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
     
#define width of candlestick elements
      width = 0.9    #for drawing open to close price
      width2 = 0.09  #for drawing high/low price

#define up and down prices
      up = df[df.Close>=df.Open]
      down = df[df.Close<df.Open]
#define colors to use
      col1 = 'green'
      col2 = 'red'
      fig, ax = plt.subplots(1, 1)
          
      #plot up prices
      plt.bar(up.index,up.Close-up.Open,width,bottom=up.Open,color=col1)
      #draw high-price line
      plt.bar(up.index,up.High-up.Close,width2,bottom=up.Close,color=col1)
      #draw low-price line
      plt.bar(up.index,up.Low-up.Open,width2,bottom=up.Open,color=col1)
      #plot down prices
      plt.bar(down.index,down.Close-down.Open,width,bottom=down.Open,color=col2)
      plt.bar(down.index,down.High-down.Open,width2,bottom=down.Open,color=col2)
      plt.bar(down.index,down.Low-down.Close,width2,bottom=down.Close,color=col2)
      #rotate x-axis tick labels
      plt.xticks(rotation=45, ha='right')
      #plt.xticks(range(1,len(df)))
      plt.title('Price: '+ str(stk[0]))
      if (cansma == True):
          sma = df['Close'].rolling(int(nday)).mean()
          plt.plot(sma, label='sma')
      if (canema == True):
          ema =  df['Close'].ewm(com=1.5,min_periods=int(nday)).mean()
          plt.plot(ema, label='ema')
      if (canb == True):
          TP = (df['High']+df['Low']+df['Close'])/3
          n = int(nday)
          sigma = TP.rolling(n, min_periods=n).std() 
          m = 2
          UBB = TP.rolling(window=n).mean() + m * sigma
          LBB = TP.rolling(window=n).mean() - m * sigma
    
    #Plot handle stick….
    
          plt.plot(UBB, label='upper')
          plt.plot(df['Close'].index,df['Close'], label="close")
          plt.plot(LBB,label='lower')
          plt.legend(loc="upper right")
          #display candlestick chart
          #plt.plot(df.Close, color="black", linewidth=0.5)
      if (strong==True):
          df['shf1'] = df['Close'].shift(-1)
          df['shf2'] = df['Close'].shift(-2)
          df['shf3'] = df['Close'].shift(-3)
          df['shf4'] = df['Close'].shift(-4)
          df['shf5'] = df['Close'].shift(-5)
          
          df['idx5'] = pd.to_datetime(df['Close'].index + pd.Timedelta(hours=120, minutes=0, seconds=0))
          
          df['idx1'] =  pd.to_datetime( df['Close'].index + pd.Timedelta(hours=24, minutes=0, seconds=0))
          df['mark'] = df['shf1']
          df['marks'] = df['shf5']
          print(df)
          i = 0 
          for index, r in df.iterrows():
            if (i>  len(df.shape)):
                i = 0
            if (r['Close'] <= r['shf1'] <= r['shf2'] <= r['shf3']  <= r['shf4'] <= r['shf5']  ):
              x = [r['idx1'],r['idx5'] ]
              y = [r['shf1'],r['shf5'] ]
              plt.plot(x,y, color="green", linestyle="dotted")
            if (r['Close'] >= r['shf1'] >= r['shf2'] >= r['shf3']  >= r['shf4'] >= r['shf5']  ):
              x = [r['idx1'],r['idx5'] ]
              y = [r['shf1'],r['shf5'] ]
              plt.plot(x,y, color="red", linestyle="dotted")
         
    @output
    @render.plot
    @reactive.event(input.gocorr, ignore_none=True)
    def plotcorrindicator():
      
      stk = input.stock()
      startdate = input.start()
      enddate = input.end()
      idxcorr1 = input.idxcorr1()
      idxcorr2 = input.idxcorr2()
      nday = input.nday()
      if ((idxcorr1 == 'rsi' and idxcorr2 == 'pctchg') or (idxcorr1 == 'pctchg' and idxcorr2 == 'rsi') ):
        df = yf.download(stk,startdate, enddate, auto_adjust=True)
        c = pd.DataFrame()
        c['pctchg'] =  df['Close'].pct_change(int(nday))
        c['rsi'] =  ta.rsi(df['Close'], length=int(nday))
        c.dropna(inplace=True)
        cvalue = c.corr()
        h = plt.subplot(1,1,1)
        h1 = h.twinx()
        h.plot(c['rsi'],color="blue",label='rsi')
        h1.plot(c['pctchg'],label='pct-chg', color="orange")
        plt.xlabel("Correlation:"+str(cvalue))
        plt.legend(loc="upper right")
        plt.title("Correlation of Technical Indicators\n"+str(cvalue))

      
      if ((idxcorr1 == 'volume' and idxcorr2 == 'rsi') or (idxcorr1 == 'rsi' and idxcorr2 == 'volume') ):
        df = yf.download(stk[0],startdate, enddate, auto_adjust=True)
        c = pd.DataFrame()
        c['volume'] = df['Volume']
        c['rsi'] =  ta.rsi(df['Close'], length=int(nday))
        c.dropna(inplace=True)
        cvalue = c.corr()
        h = plt.subplot(1,1,1)
        h1 = h.twinx()

        h.plot(c['rsi'], label='rsi')
        h1.plot(c['volume'],label='volume')
        plt.xlabel("Correlation:"+str(cvalue))
        plt.legend(loc='upper right')    
        
        plt.title("Correlation of Technical Indicators\n"+str(cvalue))
    
      if ((idxcorr1 == 'sma' and idxcorr2 == 'rsi') or (idxcorr1 == 'rsi' and idxcorr2 == 'sma') ):
        df = yf.download(stk[0],startdate, enddate, auto_adjust=True)
        c = pd.DataFrame()
        c['sma'] = df['Close'].rolling(int(nday)).mean()
        c['rsi'] =  ta.rsi(df['Close'], length=int(nday))
        c.dropna(inplace=True)
        cvalue = c.corr()
        h = plt.subplot(1,1,1)
        h1 = h.twinx()
        h.plot(df['Close'], label='Close', color="blue")
        h.plot(c['sma'],label='sma',color="orange")
        h1.plot(c['rsi'],label='rsi',color="green")
        plt.legend(loc='upper right')
        plt.title("Correlation of Technical Indicators\n"+str(cvalue))

      if ((idxcorr1 == 'sma' and idxcorr2 == 'pctchg') or (idxcorr1 == 'pctchg' and idxcorr2 == 'sma') ):
        df = yf.download(stk[0],startdate, enddate, auto_adjust=True)
        c = pd.DataFrame()
        c['sma'] = df['Close'].rolling(int(nday)).mean()
        c['pctchg'] =  df['Close'].pct_change(int(nday))
        c.dropna(inplace=True)
        cvalue = c.corr()
        h = plt.subplot(1,1,1)
        h1 = h.twinx()
        
        h.plot(df['Close'], label='Close', color="blue")
        h.plot(df['sma'], label='sma',color="orange")
        h1.plot(c['pctchg'],label='pct-chg',color="green")
        plt.title("Correlation of Technical Indicators\n"+str(cvalue))
    
      
    @output
    @render.plot
    @reactive.event(input.gocorrstock, ignore_none=True)

    def plotcorr():
      stk = input.stock()
      startdate = input.start()
      enddate = input.end()
      nday = input.nday()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      c = pd.DataFrame()
      c['0'] = df['Close'][stk[0]].pct_change() * 100
      c['1'] = df['Close'][stk[1]].pct_change() * 100
      cvalue = c.corr()
      
      plt.scatter(df['Close'][stk[0]].index, c['0'],  label = stk[0], color = "green")
      plt.scatter(df['Close'][stk[1]].index, c['1'], label = stk[1], color = "orange")
      

      plt.title("Correlation of Technical Indicators\n"+str(cvalue))
      plt.legend(loc='upper right')
      
    @output
    @render.plot
    def plotrsi():
      stk = input.stock()
      startdate = input.start()
      enddate = input.end()
      nday = input.nday()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      rsi = ta.rsi(df['Close'], length=int(nday))
      pr = pd.DataFrame()
      pr['close'] = df['Close']
      #plt.plot(pr['close'],label="close")
      #plt.show()
      pr['rsi'] = rsi
      plt.plot(pr['rsi'],label="rsi")
      x1, y1 = [df.index[0], df.index[-1]], [70, 70]
      x2, y2 = [df.index[0], df.index[-1]], [30, 30]
      plt.plot(x1, y1,  color='red', label="Overbought")
      plt.plot(x2, y2,  color='green', label="Oversold")
      plt.legend(loc='upper right')
      return 
    
    @output
    @render.image
    def image():
        from pathlib import Path

        dir = Path(__file__).resolve().parent
        img: ImgData = {"src": str(dir / "www/next.png"), "width": "70", "height":"70"}
        return img
    @output
    @render.table
    def tablereturn():
      stk = input.stock()
      startdate = input.start() 
      enddate = input.end()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      ndf =(df['Close'] - df['Close'].shift(1) )/df['Close'].shift(1) * 100
      df['return'] = ndf
      df['cumsum'] = ndf.cumsum()
     
      return   (  df.style.set_table_attributes(
                    'class="dataframe shiny-table table w-auto"'
                )
                .set_table_styles(
                    [dict(selector="th", props=[("text-align", "right")])]
                )
               # .highlight_min(color="yellow")
               #  .highlight_max(color="#AEF359")
                )    
    @output
    @render.table
    @reactive.event(input.goohlc, ignore_none=True)
    def getstock():
      stk = input.stock()
      
      startdate = input.start()
      enddate = input.end()
      df = yf.download(stk,startdate, enddate, auto_adjust=True)
      return(  df.style.set_table_attributes(
                    'class="dataframe shiny-table table w-auto"'
                )
                .set_table_styles(
                    [dict(selector="th", props=[("text-align", "right")])]
                )
               
                )
    
app = App(app_ui, server)
