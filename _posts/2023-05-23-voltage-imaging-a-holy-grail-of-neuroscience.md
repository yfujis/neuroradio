---
layout: episode
title: "#57 Voltage imaging: a “holy grail” of neuroscience"
episode_number: "57"
date: 2023-05-23
permalink: /2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/
spotify: "https://open.spotify.com/embed/episode/569NtnDLsGEwIpezY8mnIs?utm_source=generator"
apple_podcast: "https://podcasts.apple.com/us/podcast/57-voltage-imaging-a-holy-grail-of-neuroscience/id1556937028?i=1000614241627"
performers: ["萩", "脇"]
topics: ["論文解説", "イメージング", "トピック解説"]
summary: "Pieribone + Chen の in vivo 膜電位イメージング論文を題材に、遺伝学的膜電位センサー(GEVI)、広視野+高速２光子顕微鏡、U-Netベースのノイズ除去手法について掘り下げました (4/30収録)"
---

Show Notes:
[ディレクター](https://twitter.com/DonIngber)
[Allen Institute for Neural Dynamics の SAC](https://alleninstitute.org/about/people/advisors-collaborators/?_person_divisions=5)
[FMIの外部評価委員](https://www.fmi.ch/about/sab/)
[Jeremiah Cohen](https://neuroscience.jhu.edu/research/faculty/15)
[Tirin Moore](https://profiles.stanford.edu/tirin-moore)
[Thomas Mrsic-Flogel](https://www.sainsburywellcome.org/web/groups/mrsic-flogel-lab)
[Shohei Furutachi](https://www.sainsburywellcome.org/web/people/shohei-furutachi)
[NR藤島さん回](/2023/04/14/55-and-your-mouse-can-sing/)
[Krakauer](https://blam-lab.org/index.php/people/john-krakauer/)
[クラカウア―のアンチreductionistペーパー](https://www.sciencedirect.com/science/article/pii/S0896627316310406)
[NEのプレプリント](https://www.biorxiv.org/content/10.1101/2022.12.08.519670v1)
[アダム](https://alleninstitute.org/person/adam-glaser/)
[MouseLight](https://ml-neuronbrowser.janelia.org/)
[金子先生のとこの仕事](https://www.jneurosci.org/content/29/2/444)
[NRのBICCN回](/2021/10/12/27-a-rosetta-stone-for-neuroscience/)
TRIOで[LC](https://www.nature.com/articles/nature14600)とか[VTA](https://www.sciencedirect.com/science/article/pii/S0092867415008521)とか
[光学顕微鏡で見て近づいてるのを電顕で見ると半分くらいしか繋がってない](https://www.nature.com/articles/s41586-020-03134-2)
Expansionと免染でシナプス見る、例えば[コレ](https://www.nature.com/articles/s41551-022-00912-3)
[Jack](https://alleninstitute.org/person/jack-waters/)

目次
[イントロダクション](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#%E3%82%A4%E3%83%B3%E3%83%88%E3%83%AD%E3%83%80%E3%82%AF%E3%82%B7%E3%83%A7%E3%83%B3)
[Genetically Encoded Voltage Indicator (GEVI)](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#Genetically_Encoded_Voltage_Indicator_GEVI)[１．Voltage sensitive phosphataseのVSDを使った系列](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#%EF%BC%91%EF%BC%8EVoltage_sensitive_phosphatase%E3%81%AEVSD%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%9F%E7%B3%BB%E5%88%97)[1-1: VSDの末端に２つの蛍光タンパク質をつけてFRETするタイプ](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#1-1_VSD%E3%81%AE%E6%9C%AB%E7%AB%AF%E3%81%AB%EF%BC%92%E3%81%A4%E3%81%AE%E8%9B%8D%E5%85%89%E3%82%BF%E3%83%B3%E3%83%91%E3%82%AF%E8%B3%AA%E3%82%92%E3%81%A4%E3%81%91%E3%81%A6FRET%E3%81%99%E3%82%8B%E3%82%BF%E3%82%A4%E3%83%97)
[1-2: VSDのC末に蛍光タンパク質を入れるタイプ（特にpHluorine改変体）](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#1-2_VSD%E3%81%AEC%E6%9C%AB%E3%81%AB%E8%9B%8D%E5%85%89%E3%82%BF%E3%83%B3%E3%83%91%E3%82%AF%E8%B3%AA%E3%82%92%E5%85%A5%E3%82%8C%E3%82%8B%E3%82%BF%E3%82%A4%E3%83%97%EF%BC%88%E7%89%B9%E3%81%ABpHluorine%E6%94%B9%E5%A4%89%E4%BD%93%EF%BC%89)
[1-3: VSDの細胞外ループにcpGFPを挿入するタイプ](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#1-3_VSD%E3%81%AE%E7%B4%B0%E8%83%9E%E5%A4%96%E3%83%AB%E3%83%BC%E3%83%97%E3%81%ABcpGFP%E3%82%92%E6%8C%BF%E5%85%A5%E3%81%99%E3%82%8B%E3%82%BF%E3%82%A4%E3%83%97)

[2. ロドプシン系列](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#_2_%E3%83%AD%E3%83%89%E3%83%97%E3%82%B7%E3%83%B3%E7%B3%BB%E5%88%97)[2-1: ロドプシンそのものの蛍光を見るタイプ](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#2-1_%E3%83%AD%E3%83%89%E3%83%97%E3%82%B7%E3%83%B3%E3%81%9D%E3%81%AE%E3%82%82%E3%81%AE%E3%81%AE%E8%9B%8D%E5%85%89%E3%82%92%E8%A6%8B%E3%82%8B%E3%82%BF%E3%82%A4%E3%83%97)
[2-2: ロドプシンC末に蛍光タンパク質/色素を融合してFRETするタイプ](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#2-2_%E3%83%AD%E3%83%89%E3%83%97%E3%82%B7%E3%83%B3C%E6%9C%AB%E3%81%AB%E8%9B%8D%E5%85%89%E3%82%BF%E3%83%B3%E3%83%91%E3%82%AF%E8%B3%AA%E8%89%B2%E7%B4%A0%E3%82%92%E8%9E%8D%E5%90%88%E3%81%97%E3%81%A6FRET%E3%81%99%E3%82%8B%E3%82%BF%E3%82%A4%E3%83%97)

[顕微鏡パート](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#%E9%A1%95%E5%BE%AE%E9%8F%A1%E3%83%91%E3%83%BC%E3%83%88)
[Denoisingパート](/2023/05/23/57-voltage-imaging-a-holy-grail-of-neuroscience/#Denoising%E3%83%91%E3%83%BC%E3%83%88)

イントロダクション

題材とした論文：[High-speed low-light in vivo two-photon voltage imaging of large neuronal populations](https://www.nature.com/articles/s41592-023-01820-3)
[Vincent Pieribone](https://medicine.yale.edu/profile/vincent-pieribone/?tab=research)
[Jerry Chenラボ](https://www.chen-lab.org/index.html)
今回作ったプローブの解説は下のメモ1-3: SpikeyGi1&2をご参照ください
Larry Cohenラボ 、[電位センサー開発の歴史](https://medicine.yale.edu/lab/cohen/research/fluorescentsensors/)
[Larry Cohenのレガシー](https://www.spiedigitallibrary.org/journals/neurophotonics/volume-2/issue-02/021001/Pioneers-in-Neurophotonics--Special-Section-Honoring-Professor-Lawrence-B/10.1117/1.NPh.2.2.021001.full?SSO=1)
1968年から[光の複屈折（やScattering）を測定することでSquidのGiant Axonの活動電位をモニタリング](https://www.nature.com/articles/218438a0)
1973年には[Merocyanine 540 が電位感受性の蛍光色素として働くことを報告](https://www.nature.com/articles/newbio241159a0)
[giant axonだけではなくてindividual cellの活動をレポートできる](https://www.nature.com/articles/246508a0)

Genetically Encoded Voltage Indicator (GEVI)

黎明期のプローブ：

[FlaSh (Siegel and Isacoff 1997)](https://www.sciencedirect.com/science/article/pii/S0896627300809551) チャネル活性を無くしたShakerのC末に蛍光たんぱく質付加[](https://www.sciencedirect.com/science/article/pii/S0896627300809551)
[SPARC (Ataka and Pieribone 2002)](https://www.sciencedirect.com/science/article/pii/S0006349502754155?via%3Dihub) 骨格筋NaチャネルのリンカーにGFPを入れる　（１stは[イシューから始めよ](https://www.eijipress.co.jp/book/book.php?epcode=2085%EF%BC%89)の安宅氏）
[VSFP1 from Knopfelラボ (Sakai et al.)](https://onlinelibrary.wiley.com/doi/abs/10.1046/j.0953-816x.2001.01617.x) truncated K+チャネルのC末にCFPとYFPをつけてFRET[](https://onlinelibrary.wiley.com/doi/abs/10.1046/j.0953-816x.2001.01617.x)

ただし、[黎明期プローブは膜上に移行しづらく使いにくい](https://www.sciencedirect.com/science/article/pii/S0165027006004808)という問題があり、使いづらかった。
GEVI開発の難しい点は以下の通り（[St-Pierreによるレビュー](https://www.jneurosci.org/content/36/39/9977.long)を参照）：

細胞質ではなく膜上にセンサー分子が局在する必要があるため、センサーのTraffickingが良く無ければいけない
膜状にしか存在できないため、利用可能なセンサー分子の数が少ない。暗いし、SN比の要求が高い
上の問題に付随して、照射強度を強くする必要があるため、褪色が速い

SN比、Kinetics。特にKineticsは、活動電位の変化を正確に反映できるくらいの速さであるか
脱分極に対して蛍光が増えるか減るか。ベースラインが明るいとSN比が下がるし褪色も速くなる
二光子励起ができるか。ロドプシン系例のGEVIは二光子励起では使えない。
どんな色か？特にチャネルロドプシンなどと併用することができるか
電位変化に対してリニアに蛍光が変化するか。活動電位だけではなく過分極なども正確に追うことができるか
細胞毒性があるか？例えばプローブが光依存的なイオンポンプ活性等を有していたら問題

2005年に[岡村先生が報告したホヤ(Ci)由来の電位依存ホスファターゼ（VSP）](https://www.nature.com/articles/nature03650)の電位感受ドメイン（VSD）は、Traffickingが良く、これを用いたプローブが2007年から出てきた。また、2011年にはロドプシンが電位依存的に蛍光を変化させるタンパク質として使えることが報告された。2023年現在では、この２つの電位センシングモチーフが主に使われている。このメモでは、次の方針で現行プローブを整理する。方針その１：電位センシング と 蛍光の発し方 の原理別に分類。方針その２：state-of-the-art的プローブの各世代については、改良の狙い、変異アミノ酸（タンパク質のどういう機能に関連する位置か）も紹介する。
１．Voltage sensitive phosphataseのVSDを使った系列

蛍光を生じる原理の違いは３つ。1-1: VSDの末端に２つの蛍光タンパク質をつけてFRETするタイプ、1-2: C末端に一つの蛍光タンパク質、特にpHluorineをつけるタイプ、1-3: cpGFPをリンカー領域に挟むというタイプ。
1-1: VSDの末端に２つの蛍光タンパク質をつけてFRETするタイプ

最初期に出てきたもの。ただしSNがまだ弱く、kineticsも遅め（訂正：Butterfly型コンフィギュレーションではvivoでもシグナルが見えている）

[VSFP2](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0000440)from Knöpfelラボ (2007, PLOS ONE) 。CiVSDのC末にCFPとYFP
[Mermaid](https://www.nature.com/articles/nmeth.1235) from [宮脇ラボ](https://cfds.riken.jp/)＆[岡村ラボ](https://www.med.osaka-u.ac.jp/pub/phys2/okamura/) (Tsutsui et al., Nature Mthods, 2008)。海キノコから取ってきた蛍光タンパク質UKGとサンゴから取ってきた蛍光タンパク質 Kurabira-Orange (KO) のmonomeric体を作ってFRET
[VSFP-Butterfly 1.2](https://journals.physiology.org/doi/full/10.1152/jn.00452.2012)from Knopfelラボ, 2012。CiVSDのN末とC末にmKate2とmCitrinを入れてFRET。KineticsとSN比改善。
[Mermaid2と2β](https://physoc.onlinelibrary.wiley.com/doi/full/10.1113/jphysiol.2013.257048) from [筒井ラボ](https://www.jaist.ac.jp/ms/labs/tsutsui/wordpress/)＆宮脇ラボ＆岡村ラボ, 2013。

1-2: VSDのC末に蛍光タンパク質を入れるタイプ（特にpHluorine改変体）

VSDのC末に入れるタイプは、FRETもArcLightもキネティクスが遅い。しかしArcLightについては未だにGEVIの中で一番大きい蛍光強度変化を示す。

[ArcLight](https://www.sciencedirect.com/science/article/pii/S0896627312007040)from Pieriboneラボ (Neuron 2012), CiVSDのC末に[pHluorine](https://www.nature.com/articles/BF28190)（pH感受性タンパク質、eGFPに７個の変異を入れ、酸性になった時の蛍光減弱を顕著にする）。偶然入ったA227D変異（pHluorineベースの番号、ArcLightではA469D）で感度14倍に。ベースラインで明るく、脱分極に伴って暗くなる。変異pHluorineを膜貫通ドメインに近づけるとシグナルが上昇。特にC末のS249ではなくA242に使われたものか、Q239に結合したものが良く使われている（ArcLight A242 or Q239）。

[Nitabach](https://medicine.yale.edu/lab/nitabach/)による[ArcLightでのハエin vivo電位イメージング論文](https://www.sciencedirect.com/science/article/pii/S0092867413008982)
[Paul Greengard](https://www.nobelprize.org/prizes/medicine/2000/greengard/facts/)
[ArcLightメカニズム論文](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0113873)from Pieriboneラボ (PLOS ONE 2014)。実はpH sensing能は関係無くてdimerizationが重要。ArcLightと同等の変化を、CiVSD+eGFPで示すために必要十分な変異を探索。pHセンシングのためにはeGFPのS147D（ArcLight A242のS389D）だけで十分だが、この変異+A227D(ArcLightのA469D)では大きな変化は出ない。結局A227D(A469)に加えて３つの変異（ArcLightのS389D, S444F, Q446T）が必要で、これらはβバレルの一つの面に集中しており、側鎖が外側をむいている。この面は、GFPのdimerizationで使われるインターフェースの一部をなしている。pHluorineをC末にタンデムで繋ぐとArcLightっぽい変化は消失するので、これは分子内ダイマーを作っている？

[Marina](https://pubs.acs.org/doi/10.1021/acschemneuro.6b00234) (脱分極で正方向の変化を示すArcLight) from Pieriboneラボ、ACS chemical neuroscience, 2017. 先述の必要十分な変異とその近傍のアミノ酸に変異を入れていたところ、D389Aで脱分極に対する応答の方向が変わった。A389をテンプレートに再度候補配列への変異を入れていくと、H390A(GFPで言う所のH148に相当。GFPのchromophore protonation stateが変わっているのかも)とY442Vでpositiveな変化が大きくなっていった。全部hydrophobicな残基。最終的には、脱分極に対してArcLightとは逆方向で、絶対値としては1/2くらいの変化は示せるようになった。MarinaはF-Vカーブが右にシフトしていて、静止膜電位以下の過分極には殆ど反応を示さないらしい。
[Bongwoori](https://www.jneurosci.org/content/35/1/372) ArcLight系。割愛。
[ArcLightning](https://elifesciences.org/articles/10482)ArcLight系。割愛。

おまけ：pHluorine以外の蛍光タンパク質をVSDのC末に入れるタイプ

[VSFP3.1](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0002514) Knöpfelラボ, 2009年FRETでなく一つの蛍光タンパク質をＣ末につけるだけでも蛍光変化が出る。ただし、1-2%程度。Celurean, Citrin, mOrange, tagRFP, mKateといった蛍光タンパク質で試し、特にmOrangeの時にうまくいくらしい
[ElectricPk](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0043454)(Pieriboneラボ, PLOS ONE 2012): cpGFP(ElectricPk)をC末に入れている

[FlicR](https://www.jneurosci.org/content/36/8/2458.long) (Campbell, Lin, Pieriboneラボ, JN 2016) cpmApple(FlicR)をC末に入れている。赤い。これらのプローブは脱分極に対して正の方向に変化するが、HEKで比較した時にはMarinaの1/30程度の変化しか示していなさそう

1-3: VSDの細胞外ループにcpGFPを挿入するタイプ

予備知識：

GFPが光るしくみ：[Ser65–Tyr66–Gly67が自己触媒反応（特にArg96とGlu222に依る）を経て蛍光団HBIを形成し、チロシン由来フェノール基が脱プロトン化されてphenolateになると励起可能に](https://www.cryst.bbk.ac.uk/PPS2/projects/jonda/chromoph.htm)なる。脱プロトン化に主に関わる残基はHis148, Thr203, Ser205。なおフェノール基と直接相互作用するわけでは無いが、Gln94, Arg96, Glu222はHBIを脱プロトン化のために適切な位置に置くことに寄与している（[GFP変異体の構造論文](https://www.tsienlab.ucsd.edu/Publications/Ormo%201996%20Science%20-%20Crystal%20structure.PDF)）。 ちなみにGCaMP2では、GFPで言う203番目のthreonine側鎖の方向が本来あるべき位置に近づくこと、His148の代わりにCaMのArg377が水分子を介してHBIと水素結合を形成すること、が発色団の脱プロトン化に重要らしい（[GCaMP2の構造論文](https://www.sciencedirect.com/science/article/pii/S0969212608004139%EF%BC%89)）
cpGFP：GFPの円循環変異(circular permutation)では、N末・C末をリンカーで繋ぎ、144番目の残基と145番目の残基新しくC末・N末としているものが主流。つまり、GFPのHis148はcpGFPではHis4となる。上記のCa2+結合時GCaMP2の結晶構造を見るとわかるように、HBIの脱プロトン化に関わる残基はGFPと類似しているが、必ずしも一致せずともよい（脱プロトン化できる限りは）
cpsfGFP-OPT：GFPにF99S, M153T, V163A + F64L, S65T + S30R, Y39N, N105T, Y145F, I171V, A206Vという変異を入れたのが[superfolderGFP](https://www.nature.com/articles/nbt1172)。更に[splitGFP](https://www.nature.com/articles/nbt1044)のGFP1-10で使われていた、solubilityとfolding kineticsを最適化するために入れた７変異（N39I, T105K, E111V, I128T, K166T, I167V and S205T）が入ったのがsfGFP-OPT。普通のcpGFPと同じく144-145番目の残基で円循環変異。

[ASAP1](https://www.nature.com/articles/nn.3709) from [Michael Linラボ](https://linlab.stanford.edu/), NN 2014。[Francois St-Pierre](https://www.stpierrelab.com/)が筆頭。VSDベースでキネティクスが良いモノを作るのが目標。VSDは4回膜貫通型タンパク質であるが、そのHelix３-４間のextracellular loop ((143)SDLAATDQMPR(153)のうち、A147-T148の間) に円循環変異を施したGFPを入れている。脱分極すると暗くなるタイプのプローブ。CiVSDはcpGFPをこの位置に入れると膜移行が悪くなるらしく、チキン由来のVSDを利用（GgVSD。細胞外ループが11残基でCiVSDの15より短い。ちなみにWTのVSDではなく、電位依存性のレンジをシフトさせるR153Qや、発現量を上げるために開始コドンの後に１コドンを挿入するといった改変アリ）。入れるGFPはGCaMP3で使っているcpGFP, cpClover, cpsepHluorine, cpsfGFP-OPTの４種を検討し、cpsfGFP-OPTだとうまくいく。cpsfGFP-OPTはペプチド付加したり円循環変異を入れてもfoldしやすい, 等の特徴があるGFP変異体。ArcLight Q239に比較して、分散培養で活動電位を見た時はΔF/Fが２倍ほど良いとか、HEKでスパイクトレイン的な電位変化をした際の時間解像度がArcLightの30 Hz程度に比較してASAP1だと200 Hzまで行ける、とか。ちなみに検討の過程で、SN比は悪いがpositiveな変化を示すvariantが取れている。cpGFPのbreak pointを144-145ではなく、146-147、あるいは147-148. 148-149にしたもの（サプリFig 3）。
[ASAP2s](https://elifesciences.org/articles/25690)(eLife 2017): St-Pierreがラストオーサーの仕事。VSDのvoltage sensingしそうな部位（helix1と4）に置換変異。Helix4のR415Qがアタリ、HEKを使ったアッセイでは脱分極に対する感度がASAP1に比較して66%程度上昇。分散培養の心筋細胞で見た時は２倍くらい、ArcLightの1.5倍くらい。キネティクスはASAP1より数10%程度遅くなるが、それでもArcLightより３倍くらい速い。ニューロンで見た時は、ASAP1より50-60%程度感度が良い。
[ASAP2f](https://www.sciencedirect.com/science/article/pii/S0092867416305827)Lin と[Clandini](https://flyvisionlab.weebly.com/)のコラボ、 Cell 2016,  St-Pierreは2nd。cpGFPとVSD Helix3 のlinkerを置換＆削る（A147S, delta A148）。ハエでin vivo 2 photonイメージング。ASAP1からkineticsは変わらないまま、感度が20%前後上がっている。特に過分極への感度がより強く上がる。なお、linkerアミノ酸のナンバリングがASAP1から１個ずれている（SDLS&lt;削除&gt;&lt;cpsfGFP-OPT&gt;TDQMPQの最初のSが143ではなく144番目に。ASAP1のA147とA148がASAP2fのA146とA147に相当）が、これは、ASAP1論文のナンバリングはWTのVSDに準拠しており、ASAP2f論文のナンバリングではメチオニンの後に入ったコドンをカウントしているためと思われる。
[ASAP3](https://www.sciencedirect.com/science/article/pii/S0092867419312255)Linラボ, Cell 2019。 2fと2sの変異を両方取り入れつつ、2fで改変の対象としたリンカー近傍について、変異を入れる範囲を広げている。146から151まで。147まではCiVSP由来の配列だが、それ以降はcpGFP由来配列。つまりASAP3の148-151番目の残基はcpGFPの1-4番目の残基に相当（４番目のHistidineはGFPでは蛍光の発生に必須の残基。下記の補足を参照）。２残基ずつsaturation mutagenesisやって有益lなものを採用（ L146G, S147T, N149R, S150G, H151D, R414Q ）。S147T はASAP2fの変異をoverwriteした形、R414Q は2sの変異に相当。スライスで見た時にASAP2sよりSN比が50%くらい高くて、Kineticsはriseが2sより若干はやくなり、decayは大差ない。2pでin vivoでマウスの脳活動が見える。
[ASAP4](https://www.biorxiv.org/content/10.1101/2021.10.21.465345v3)Linラボ、bioRxivプレプリント。positiveな変化を示すことが目標。発色団と相互作用しうる151番目のHistidineとその隣の150 Serineが変異の候補。ASAP2f L146G, S147T, R414Q (ASAP3から149-151 の変異を抜いたもの) をベースに、150と151の全ての組み合わせ、400変異体をテスト。S150D H151G (ASAP4.0) は、 HEKで見た時、–70 mV to +30 mV にかけて正の方向への変化。しかもダイナミックレンジがASAP3の２倍。ただし、蛍光変化 vs 電位変化カーブのレンジが生理的な電位変化レンジと合っておらず、right-shiftしている。そこで、これをleft-shiftさせる変異を探した。発色団と相互作用する別の残基であるThreonine 206 (GFPのThr203)をmutagenesis。T206Hにしたところ、蛍光変化 vs 電位変化カーブがleft-shiftして生理的な電位変化のレンジで蛍光変化がおさまるようになった（ASAP4.1）。ただし、-70 mVにおける蛍光も上がってSN比が下がった。そこで、150,151と相互作用しそう、かつVSDの動きをcpGFPの構造変化に繋げるのに重要そうな148と149の残基についての変異400通りを全部試したところ、F148PとN149Vが-70mVでの蛍光を下げた（ASAP4.2）。更に、Helix4のF413に変異を入れて-70mVでの蛍光を下げることを狙った。結果として、vivoでSSTニューロンの1 photon imagingをした際にASAP3と遜色ない程度のSN比で、かつ反応方向が逆なものができた。F413V (ASAP4.3) and F413G (ASAP4.4 4b, brighter baseline). F413M (ASAP4.5, 4e enhanced response)。
[JEDI-2P](https://www.sciencedirect.com/science/article/pii/S0092867422009163)St-Pierreラボ、Cell 2022.  １光子イメージング時に性能改良に寄与する変異が２光子イメージング時では性能改良に寄与しないこともあることに着目し、最初から２光子を使ってスクリーニング。ASAP1と2sベース。21箇所（13箇所がVSD関連、8箇所がcpGFP関連）のアミノ酸をsaturation mutagenesis。まずASAP3と似たような発想で、リンカーの147番目の残基から、発色団とinteractionするhistidineまで（さっきは151だったがASAP2sベースなので152）を変異。発色団の脱プロトン化に関わるもう一つの残基に相当するT207も変異（cpGFPのT203）。加えて、これまでにASAPシリーズでターゲットにされていたhelix3とcpGFPのリンカーだけでなく、helix4とcpGFPのリンカーも変異。389, 390, 391, 393, 394, 397。ちなみに392までがsfcpGFP-OPT由来で、393からがVSD由来。397が WTのVSDのR153Qに相当。他には、helix4内の403,409,412,415、あと別のヘリックス内のD105, D127, N124。進化的に保存されている残基を狙ったとのこと。最終的に残った変異はASAP2sをベースにしてN124V, H152E, T207H, N391D, Q397H, R406K, Q415R。152と207は上述の通り発色団とinteractionする場所で、391と397がこれまでいじられてこなかったリンカー部位（ASAP1で有益と思われていたR397QがHに変わっている）。124と406はVSDでこれまでいじられてこなかったところ、そして2sで入れたR415Qが元に戻っている。パフォーマンスとしては、vitroで２光子で見た時にはASAP2, ASAP3より1.5倍明るく、ΔF/Fも2.5倍程度。vivoでマウスの脳活動が見えることを示している。ちなみに、二光子で見た時、ASAP3の感度や明るさはASAP2と殆ど変わらないらしい。
[SpikeyGi1&2](https://www.nature.com/articles/s41592-023-01820-3) Pieriboneラボ, Nature Methods 2023. positiveな変化を示すことが目標。ASAP3 に２種類の改変を追加。①電位感受性ドメインの細胞外ループとcpGFPの接合部（と著者らは言っているが、cpGFPの残基で発色団とinteractionする位置のはず。あと、収録中Marinaの変異と似てないと言いましたが、前段階の検討で入れているASAP2fへのH150(151の間違い？)点変異はcpGFPがeGFPの配列だったとすると同じ箇所H148に相当する場所かもです…すみません）である151-152番目のアミノ酸の間に2アミノ酸の挿入をする形でsaturation mutagenesis。DSを入れたらpositive goingが強くなる（これがSpikeyGi）、②cpGFPのV170をIに置換したというもの（これがSpikeyGi2）。これによって感度が上昇。結果、vitroのスライスで見た時にdelta F/F0がASAP3と同等かそれ以上、kineticsはASAP3とriseは同等でdecayがちょっと遅い程度のパフォーマンスを、逆方向の変化で示す変異体ができた。スクリーニングはAdam Cohenラボの [Spontaneously Spiking HEK293 (NaV1.3とKiR2.1を入れたHEK)](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0085221)で行っている（最新の、ドキシサイクリンでKirのエクスプレッションを制御するやつ＆CheRiffを発現させたやつ、では無い）。なお、HEKで見た時、矩形波の入力に対してのresponseはASAPでは矩形波っぽくなるがSpikeyGi達は最初に大きな変化が出た後に急激にdecayしているように見える（Fig. 1d）、ただしこれはHEKのCaダイナミクス特有のもので、ニューロンでは大丈夫らしい（Fig. 2b）。2Pでも使える（Fig 2）。evoked活動でestimateされるスパイク数はASAP3より多いため、SN比が高くなっていることが推測される。continuousなillumiationで見た時はASAP3と同程度のphotobleachingだが、intermittentなilluminationで見た時はphotobleachingが低減される（Fig. 6a、正直、意外と低減されないんだな…という印象）。なおV170はGFPでいう所のI167で、super folderにする過程で入れた変異が元に戻った形。

2. ロドプシン系列

蛍光を生じる原理の違いは大きく分けて２つ。2-1: ロドプシンそのものの蛍光を見るタイプと、2-2: ロドプシンの末端に蛍光タンパク質、あるいは蛍光色素をトラップするタンパク質を結合して、ロドプシンとのFRETで観察するタイプ。
2-1: ロドプシンそのものの蛍光を見るタイプ

予備知識：

ロドプシンのPhotocycle（[神取先生レビューも参照](https://seikagaku.jbsoc.or.jp/10.14952/SEIKAGAKU.2019.910472/data/index.html)）：Gground stateから550 nm光を受けることでレチナールの構造が光異性化して13-cisになり（L）、シッフ塩基から細胞外側の残基へのプロトン転移が起こり（M1）、シッフ塩基が細胞質側の残基からプロトンを受け取れるようになり（M2）、プロトンドナーがシッフ塩基にプロトンを渡して（N）、プロトンドナーが細胞質からプロトンを取りつつレチナールが熱異性化によってall-transに戻り（O）、acceptorがプロトンを細胞外に出す（ground stateに戻る）。このようにground state→L→M1→M2→N→Ｏと回っている
[電位依存的に光る仕組み](https://www.pnas.org/doi/10.1073/pnas.1215595110)：Cohenラボ, PNAS 2012。Ｎの時に540 nmの光を受けるとQというstateに代わって、Ｑの時に570 nmの光を受けると強い蛍光を発する。なお、普通ロドプシン業界で使われるQ stateというのは別のstate(OからPというstateを取ってQというstateに行くルートがある)の事を指しており、[本論文中でのQ stateはOhtaniさんが見つけた](https://www.sciencedirect.com/science/article/pii/001457939280643U)のでOhtani Qと呼ばれている。電位が変化するとシッフ塩基からプロトン転移が起こるstateとプロトンをもらうstateの平衡が変わり、Nになりやすくなるため蛍光変化として検出できる。なお、Ohtani Q のstateでレチナールがどういう構造を取っているのかは明らかでは無いらしい。
DTDモチーフ：シッフ塩基からプロトンを受け取る細胞外側のD（プロトンアアクセプター。バクテリオロドプシンだとD85、ArchだとD95、Ace2だとD81）や、脱プロトン化されたシッフ塩基に細胞内側からプロトンを渡すD（プロトンドナー。バクテリオロドプシンだとD96、ArchだとD106、Ace2だとD92）を含むモチーフ。DをNにするとプロトンの受け渡しができなくなり、ポンプ活性は殆どなくなる。モチーフがDTDまたはDTEであればプロトンポンプ、NDQであればナトリウムポンプ、カルボン酸を持たなければ（NTQまたはTSA）クロライドポンプ、らしい。プロトン輸送機構の詳細は[前田先生レビュー](https://www.jbsoc.or.jp/seika/wp-content/uploads/2013/11/80-11-02.pdf)、クロライドポンプとの違いなどは[菊川先生レビュー](https://www.jstage.jst.go.jp/article/biophys/61/1/61_012/_pdf)が分かり易い。

[PROPS](https://www.science.org/doi/10.1126/science.1204763)[Adam Cohen ラボ](https://cohenweb.rc.fas.harvard.edu/), 2011, Science。最初にロドプシンが電位センサーとして使えることを報告した仕事。Proteorhodopsin optical proton sensor の略。大腸菌で電位が蛍光変化として観察可能であることを報告しているが、その後あんまり使われていない。
[Arch](https://www.nature.com/articles/nmeth.1782)Cohenラボ, 2011, NMeth。抑制性オプトジェネティクスツールとして使われるArcheorhodopsinが、電位依存的に蛍光強度を変化させることを報告した仕事。pHを7.3から11.1に変えると色が変わる…ので、シッフ塩基の脱プロトン化がChromophoreに影響する？という観察結果から、local electrochemical potentialの違いもプロトン環境の変化を引き起こし、同じようにChromophoreの変化を起こすのではないかと考察。640 nmのレーザーを当てて687nmの蛍光（peak 710 nm）、ph7だと蛍光あるけど10だと無し。パッチして電位を変えながら蛍光を観たところ-150 mVから150 mVに上げるにつれて蛍光が変化（ASAPだとシグモイドだったが、ほぼリニアな変化）。プロトンポンプ様の活動を示すための照射波長は588 nmだが、640 nmでも若干活性がある。ただしプロトンポンプ活性を止めたD95Nもセンサーとしての機能を示す。-150mVから150mVでWTより３倍程度のダイナミックレンジ。でもキネティクスが若干遅い。脳スライスで使えることを示している。
[QuasAr1,2](https://www.nature.com/articles/nmeth.3000)Cohenラボ (NMeth 2014)。ポンプ活性が無く、kineticが速く、明るいArch変異体を得るのが目的（更に言うと吸光スペクトルが青側にシフトしたチャネルロドプシンCheRiffと併用してall opticalな生理学、optopatchを行うのが目的）。大腸菌ベースのスクリーニング。Random mutationにより明るい変異体を得る。P60S, T80S, D95N, D106Y, F161Vが有益な変異として釣れてきた。また、trafficking改善のためにC末のVSAADRPVVAを３残基のアミノ酸で置換し、TLMが一番良いモノとして釣れてきた。次にD95N, D106Yを標的として変異を入れた。ここはバクテリオロドプシンのD85とD96に相当し、DTDモチーフをなす残基（95がプロトンアクセプターで、106がドナー）。HeLaで電位変化に対する応答を見ながら全変異について探索。D95HとD106Hが望む特性に近い変異体となった（QuasAr1）。D95QがQuasAr2。QuasAr1はArchと同じくらいの明るさとキネティクスでポンプ活性は無い。QuasAr2はArchの２倍程度明るくポンプ活性も無いが、若干遅い。脳切片で使えることを示している。
[QuasAr3, paQuasAr3](https://www.nature.com/articles/s41586-019-1166-7)Cohenラボ (Nature 2019) vivoでQuasArを使えるよう発現量とtraffickingを改善するのが目的。rationalなengineering、C末への付加配列、リンカーの最適化。QuasAr3はQuasAr2にK171Rという点変異を入れ、C末にTS-citrin-TS-TS-TS-ERという配列を入れたもの。K171は細胞内ループ上の残基でユビキチン化の標的になるため、Ｒにして分解が押さえることが発現量上昇につながる。TSはKir2.1のtrafficking signalで、Citrinは蛍光たんぱく質、ERは小胞体移行シグナル。paQuasAr3では、V59Aという変異が追加される。BacteriorhodopsinのV49Aに相当する変異で、吸光上昇が見られるらしい。赤色光で励起しても何も変化はなかったが、青色光を当てながら赤色光を当てて電位変化を見ると、蛍光が全体的に上昇、約３倍に。SNRも約２倍程度に上昇。青色光を当てることによってM stateからN stateの状態が増え、結果としてQ stateにも移行しやすくなっているのではないか、という考察。あと、V59A変異を入れておくと何故かmembrane traffickingが改善するらしい。vivoのマウスで神経活動見ています。
[Archon](https://www.nature.com/articles/s41589-018-0004-9)Boydenラボ（Nature Chemical Biology 2018）。QuasAr2を更に明るく、膜移行良く、感度良くするのが目的。副産物として褪色が遅いものが得られた。QuasAr2にエラープローンPCRを施したライブラリをHEKに発現させ、顕微鏡の画像に基づき、明るさや膜への移行、電位感受性等のパラメーターが良い５細胞をピペットで釣ってきてシーケンシング。5つの変異体のうち4つの変異体でT56、T117、T183、L198に変異が入っていたほか、αヘリックスに４つ（T20S、L31V、K47R、A137T）、βストランドに2つ（S80PとD88N）の変異が見られた。次のラウンドでは、同定した有益な変異箇所に対してtargeted mutagenesis＆レチナールが結合するシッフ塩基の近傍に変異を入れた。また、C末にtrafficking signalとEGFP, ERをつけて膜移行を良くしている。結果として得られた変異体Archon1 （QuasAr2 + T20S/G41A/V44E/S80P/D88N/A137T/ T184I/L199I/G242Q）およびArchon2 （QuasAr2 + T56P/S80P/H96Q/T100S/H108D/T118I/T184I/L199I/A226C) は、HEK細胞の細胞膜上によく局在し、QuasAr2と比較してそれぞれ2.4倍および6.8倍明るい。100mVの電圧変動に対するArchon1およびArchon2のHEK細胞でのΔF/Fは、それぞれ81±8%、20±2% （QuasAr2では46±4%）。狙っていたわけでは無いがArchon1は900sの照射後も95%の蛍光を維持していて、Archon2より３倍、QuasArより５倍褪色が遅かった。マウス脳スライスやゼブラフィッシュ、線虫で使えることを示している。
[Archer](https://www.nature.com/articles/ncomms5894)Gradinaruラボ。割愛。
[QuasAr6a,b](https://www.nature.com/articles/s41592-022-01743-5)Cohenラボ (Nature Methods 2023)。同じくエラープローンPCR。スパイクが出るHEKでスクリーニング。CheRiffと共にmEOS4aという光照射で緑から赤に変わる蛍光たんぱく質を共発現させ、良いvariantをマーキングしてFACSで釣る。見つかった変異を併せてみたが、３次元的に近いアミノ酸同士の両方に変異を入れると、膜移行に壊滅的な影響が出る事が多かった。そこで、タンパク質構造の情報を用いて遠く離れている箇所の変異を選んできた。明るくなる変異 (W42G, V124G, R237I, A238S) と、発現量が上がる変異(M85I, F98L, W148C) 。結果として、QuasAr6a (Archon1 + W42G/M85I/F98L/V124G/ W148C/A238S)とQuasAr6b (A238Sの代わりにR237I）が取れた。QuasAr6aはkineticsに優れ、QuasAr6bは明るい。また、Archon1はC末にTS-EGFP-ER2をつけていたが、これをQuasAr3で用いていたTS-Citrine-TS × 3-ER2に変更した。Sliceで見たところ、aとbはArchonに比べて数10%速くて数10%明るい。vivoでもQuasAr6の方がArchonよりSNRとkineticsが優れているというデータ。なおQuasAr3で入れていた点変異は消えた。

オプシン型のものは２光子では励起できないという問題がある。 Archベースのプローブは頭うちになっている感。Archとかより他のロドプシンを探した方が良いか。例えば近年見つかった[ヘリオロドプシンなどもセンサー様の動きを示す](https://www.biorxiv.org/content/10.1101/2023.03.27.534354v1)らしい。２光子励起ができるようなやつもひょっとしたらいるかも？
2-2: ロドプシンC末に蛍光タンパク質/色素を融合してFRETするタイプ

ロドプシンのC末端に蛍光たんぱく質をつけて励起。電位依存的な構造変化が起こって、蛍光たんぱく質がロドプシンに近づいた時にFRETが起こり、暗くなる。つまりロドプシンが電位センサーかつFRETアクセプターとして働く。ロドプシンより励起に必要なレーザー強度が少なくて済み（1/50~1/100程度）、ロドプシン単体のものほどではないがキネティクスが速い（ASAP系よりも速い）。

[Ace2N-mNeon](https://www.science.org/doi/10.1126/science.aab0810)[Schnitzer lab](https://pyramidal.stanford.edu) (Science 2015)。これ以前に同じ原理のものとして[MacQ-mCitrine](https://www.nature.com/articles/ncomms4674)（Schnitzer, Nat Comm 2014）や[QuasAr2-EGFP/Citrin/mOrange/mRuby/mKate](https://www.nature.com/articles/ncomms5625)（Cambell & Cohen, nat comm 2014）などが報告されていたが、Ace2N-mNeonが一番良く知られている。Aceは吸光スペクトルがブルーシフトしたロドプシンで、FRETパートナーとして他のロドプシンよりより優れている。あとキネティクスがMacの６倍速い。mNeonGreenは緑色蛍光たんぱく質の一種で、明るくて褪色が遅い。Ace由来のロドプシンは1と2の２つがあり、それぞれAce1-D89Q(Ace1Q), Ace2-D81N (Ace2N)っていうポンプ活性を弱めた変異体を作成。２アミノ酸（SG）のリンカーを使ってAce1Q or Ace2NとmNeonGreenを結合。2Nの方がspike detectionのfidelityが高い。培養ニューロンで見た際はAce2NはArcLightやASAPよりSN比が３倍近く高く、圧倒的に速い。ただし膜移行性は低く、vivoではそのまま使えない。リンカーを４アミノ酸にすると発現量が上がり、vivoでも使えるように（Ace2N-4aa-mNeon）。ただし４アミノ酸で繋ぐとロドプシンと蛍光たんぱく質の距離が離れるのでFRET効率は下がる。
[VERNAM](https://www.nature.com/articles/s41592-018-0188-7) SchinitzerとPieriboneのコラボ, Nature Method 2018。AceとmRuby3のFRETで、赤色のものを作るのが目的。ただしmNeonを単純にmRuby3に代えただけだとFRET効率が悪い。そこで、リンカーの長さを変える＆Ace2N吸光波長のレッドシフト（retinal binding pocketのエンジニアリング）による解決を狙う。288種類のリンカー変異体をスクリーニングした結果、N側にWRの２残基を挿入した変異体Ace-WR-mRuby3でコントロールの約1.4倍反応性が上昇。また、768種類のretinal binding pocket変異体を試し、Ace-WR-mRuby3 N81Sで約2倍感度が上昇。N81Sとホモロガスな変異は他のロドプシンで吸光スペクトルをレッドシフトすることが知られている。培養ニューロンでAce2N-mNeonと同じくらいのパフォーマンスを示すものが得られて、スライスでもシグナルが取れた。
[Ace-mNeon2, VERNAM2](https://www.science.org/doi/10.1126/science.abm8797)SchinitzerとPieriboneのコラボ, Science 2022。それぞれの感度を上げるのが目的。狙った箇所は、リンカー領域と、D81N (non-pumpingにするために最初に入れた変異、DTDモチーフの一つ)。Ace2N-mNeon N81S G229YがAce-mNeon2で、VARNAM Δ228W Δ229R G231IがVARNAM2。つまりVARNAM作るときに入れた２個のリンカーWRがどっちもはずれて、SGのリンカーのうちGがIになった。HEKでの比較では全世代から約３倍、２倍程度の感度。vivoで使えている。
[pAceとpAceR](https://www.science.org/doi/10.1126/science.abm8797)pAceとpAceR SchinitzerとPieriboneのコラボ, Science 2022 (同じ論文)。ここまでのFRETでは脱分極に応じて暗くなるタイプだが、明るくなるものを作成。まずAce-mNeon2 D92のsaturation mutagenesisから。この残基はDTDモチーフの、細胞質側プロトンドナーに相当。D92Nにしたときに反応方向の正負が逆転。ただしkineticsが遅かったので、S81Xのsaturation mutagenesis。S81Dにしたらそれなりに早いし一番大きいが電位感受性が得られた（つまりプロトンポンプ活性を阻害するためにAce-mNeonでNにしたD81(プロトンアクセプター)がAce-mNeon2でSに変わり、Dに戻っている）。なお、後述のVoltronをPositronにした時の変異と同じ。更に、３番目のtransmembrane helix（DTDモチーフのD81とD92を含むhelixで、MかNの中間体構造をstabilizeするのに重要な残基を多く含むらしい）に変異を入れた。結果、Ace-mNeon2 R78K S81D D92N W178F と VARNAM2 R78E S81D D92N ならばAce-mNeon2やVARNAM2と同じかそれ以上の感度が得られることが分かり、それぞれpAce (positive Ace) と pAceR (positive Ace in Red)と命名。pAceR以外はサブミリ秒のkineticsを維持しており、アクションポテンシャルを十分レポート可能。pAceRは遅いが、TableS1によるとHEK 239においてはASAP4と同程度。
[Voltron](https://www.science.org/doi/10.1126/science.aav6416)Janeliaの[Eric Schreiter lab](https://www.janelia.org/lab/schreiter-lab)から、Science 2019。蛍光タンパク質をベースにしたFRETセンサーは褪色が速いので、代わりに褪色に強い蛍光色素を使おうという発想。mNeonの代わりにHalo-tagを入れて、Halo-tagがJaneliaが作った[JF-dye](https://www.nature.com/articles/nmeth.4403)に結合する。リンカーの最適化（junctionのアミノ酸を５個削る）を行うと一番良いSN比が得られる。Ace2NとJF525ないしJF549でFRET、これをVoltronと呼ぶ。培養ニューロンで比較したところ、Ace2N-mNeonより3-4倍明るくて、褪色にかかる時間は約７倍。vivoでも使える。ただし、これも１光子のみでしか使えず、二光子では使えない。
[Positron](https://www.nature.com/articles/s41467-020-17322-1)Eric Schreiter lab (Nat Comm 2020)。脱分極に伴って明るくなるvoltronを作るのが目的。pAceやpAceRよりも先。Ace2Nでは細胞外側にあってプロトンアクセプターとして働くD81がNになってポンプ活性が止まっている。電位感受性はレチナールが結合するシッフ塩基と細胞質側にあるプロトンドナーとなるD92との相互作用により起こっている。そこで、細胞内側のプロトンドナーとの相互作用を止め、細胞外のプロトンアクセプター側と相互作用させれば、膜電位の変化に対して逆の反応を起こせるのではないかと考案。まずプロトンドナーのD92を不活性なNにしたところ、photocurrentは blockできたし、反応性が逆になった。ただし、キネティクスが遅くなった。そこで、Ace2Nで入れていたプロトンアクセプターのD81NをDに戻した。すると、活動電位を追うのに十分なキネティクスが得られた。ただし、微妙にphotocurrentが出る。SN比がvoltronの40%程度だったので、プロトンを細胞外側に運ぶ経路（189と199番目の残基）をエンジニアリングしたところ、E199Vにしたときに２倍近いダイナミックレンジが得られた。これによりSN比はvoltronとほぼ変わらず、静止膜電位の時は暗くて脱分極に応じて明るくなる変異体、positronが得られた。比較は主にHEKか培養ニューロンで行い、zebrafishで使えることまで示している。Voltronより更に褪色しづらくなり、他のロドプシンにも応用可能であることを示している。

おまけ：

第三の原理：[hVOS](https://www.nature.com/articles/nn1558) (hybrid Voltage Sensor): 脂溶性だが電荷のある蛍光色素DPAが、電位に応じて細胞外側（過分極時）細胞内側（脱分極時）によるかという性質を利用するプローブ。膜にアンカリングしたGFPを細胞内側に出しておくと、脱分極の時にDPAが近づいてきて、DPAはGFPの蛍光をabsorbするのでFRETが起こる。
Yuste達が[side-by-sideで比較した論文](https://www.sciencedirect.com/science/article/pii/S2211124718320485)が2019年に出ている。 比較したのは、ArcLight-Q239と、ArcLight-Q239にTSとERをつけたArcLightMTと、ASAP1, 2s, 2f, Ace2N-4aa-mNeon, QuasAr2, Archer。培養ニューロンでのSN比はAce2NとかQuasAr系が良い。ArcLightとかASAP系はどっこい。kineticsはAce2NとQuasAr達が桁違いによく、100 Hzまでしっかり。ASAP系は40Hzが見えるか見えないかという感じで、ArcLightは10Hzでギリ見えるかという感じ。褪色はAce2Nが速い。In vivo 1 photonでは、オプシン系は暗すぎて見えないので検討から外れる。１光子で応答が見えたのはArcLightMTだけで、２光子だと程度は若干弱まるけどASAP系もOK。
[StayGold](https://www.nature.com/articles/s41587-022-01278-2) がモノメリック体かつcpGFPとして使えるようになったら褪色の問題は改善するかも？
[mNeonベースのGECI](https://www.nature.com/articles/s41592-023-01852-9)
[モノマーで明るいの取ってきたらNature Methods](https://www.nature.com/articles/s41592-023-01809-y)
[Yuste, PSDにくっつける](https://www.science.org/doi/10.1126/science.abg0501)

顕微鏡パート

Jerry Chenの[CRACK](https://doi.org/10.1126%2Fscience.abl5981)。と[それを読んだNR回](/2021/03/24/4-what-is-cell-type-transcriptome-meets-neurophysiology/)。
[Elly Nedivi](https://nedivilab.mit.edu/), [Peter So](https://web.mit.edu/solab/)との[共著の仕事](https://doi.org/10.1016/j.neuron.2012.02.030)。抑制性シナプスのクラスタリングを見たもの。
広域顕微鏡開発で使われたTemporal Multiplexing
単純な仕組みとはいえ、&lt;10nsの時間解像度でシグナルを処理するFPGAの設計は結構トリッキーらしい([Kaspar](https://alleninstitute.org/person/kaspar-podgorski/)談)。
2x

[Jerry Chen, Fabian Voigt, Helmchenの広域顕微鏡](https://doi.org/10.7554/eLife.14679)
Spencer Smithの[Trepan2p](https://doi.org/10.1038%2Fnbt.3594)

4x

[Chen, Spencerの広域顕微鏡](https://doi.org/10.1038/s41467-021-26737-3)
Spencerの[Diesel2p](https://doi.org/10.1038/s41467-021-26736-4)

[](https://doi.org/10.1038/s41467-021-26736-4)Spatial Multiplexingはそれこそ[Peter Soが先駆け](https://opg.optica.org/oe/abstract.cfm?uri=OE-15-18-11658)GFPの蛍光が2~3nsなので8nsのtemporal delayではcross-talkないのでは...と言っていますが、これは光子数が1/eになる時間なので、e^3~=20から、ざっくり全蛍光の5~10%くらいは漏れ込んでもおかしくないことになります。
他

[2p RAM](https://elifesciences.org/articles/14472)
Kasper の[トモグラフィー](https://www.nature.com/articles/s41592-019-0493-9)
[Na Ji](https://www.jilab.net) の[ミラー](https://www.nature.com/articles/s41592-020-0762-7)
Fixed wavelength の femtosecond laser ([Alcore 920](https://spark-lasers.com/produit/alcor/))
[Pre Chirpとは](https://www.pneum.co.jp/note/benefits_of_ultrashort_pulses/)
[Mai Tai の Deep See](https://www.spectra-physics.com/en/f/mai-tai-deepsee-ultrafast-laser)
[Coherentの可変波長レーザー](https://www.coherent.com/lasers/ultrashort-pulse)

Denoisingパート

Self-supervisingの説明を簡略化のために[DeepCAD](https://www.nature.com/articles/s41592-021-01225-0)を例に用いて行いましたが、DeepVIDではspatialなinterpolationも行われています。ターゲットにするフレームの10%(この値はハイパーパラメタサーチの結果empiricalに決めている)をblindにしておいて、L2の計算をこのblind pixelsのみに対して行うことで、spatialな情報も利用するようになると考えられます。Shot-noiseはtempora/spatialともに独立なノイズになりますが、signalはspatialにもlocal correlationが高いことが多いので、ノイズだけが主に消えることになると考えられます。

元になったアーキテクチャ・フレームワーク
[Ronneberger](https://lmb.informatik.uni-freiburg.de/people/ronneber/)らによる[U-Net](https://lmb.informatik.uni-freiburg.de/people/ronneber/u-net/)と[3D-U-Net](https://arxiv.org/abs/1606.06650)U-Netを元にしたノイズ処理の元ネタ: [Noise2Void](https://arxiv.org/abs/1811.10980)

[DeepInterpolation](https://www.nature.com/articles/s41592-021-01285-2)
[Kenneth HarrisじゃなくてArthur Konnerthですね](https://www.nature.com/articles/nature08947)…汗
[GCaMPのブログ](https://tak38waki.hatenablog.com/entry/2018/02/14/233602)

Editorial Notes:
タンパク質構造予測でドッキングシミュレーションとかまでできるようになってきたみたいですが、構造のデータに基づいて、rationalに、センサーのリンカーはどのくらいの長さでどの配列が良いのか、とか、どこにどういう変異を入れるとどういう性能が上がるか…みたいなのは予測できたりするんでしょうか。[Lin Tianの](https://www.sciencedirect.com/science/article/pii/S0092867420316123?via%3Dihub)は配列データだけで構造の情報はあんまり使えて無さそうだし。それはさておきQuasAr4,5をご存知の方はこっそり教えてください笑（脇）
VoltronシリーズのEricがオプシンベースのやつも2p励起で動くとか最近の[オプティカ](https://www.optica.org/en-us/home/)で言ってたらしい。タイトルはBando, Yusteのreview、&quot;...in a way a “holy grail” of neuroscience, could be carried out by imaging membrane potential.&quot;より。 (萩)
