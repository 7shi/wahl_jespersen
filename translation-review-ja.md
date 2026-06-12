# en-ja.md 日本語訳レビュー

対象: `en-ja.md`（英語原文と日本語訳の対訳ファイル、全372行）
レビュー日: 2026-06-13
方針: レビューのみ。修正は保留。行番号は en-ja.md のもの。

## 総評

セクション I・II（〜126行目あたり）は比較的整った訳文だが、セクション III の O.J. の派生論（167行目）以降、品質が急激に低下する。後半は機械翻訳の生出力に近い状態で、以下の問題が集中している。

- 意味が反転・破綻している誤訳（indispensable→「使えません」、genitive→「主格」など）
- 固有名詞・術語の取り違え（Ido→「井戸」、accusative→「非難語」、namely→「ノミム」など）
- 文単位の訳抜け
- 英語原文がそのまま残っている箇所
- Markdown の `*`（イタリック記号）の崩れ、文の重複、括弧の不対応

git ログに「fix ja (III) partial」とあるとおり III の途中までは手当て済みと見られ、実際に問題の大半は III 後半（167行目〜）から V にかけて残っている。

---

## A. 重大な誤訳（意味の反転・破綻）

### A-1. L17: 「省略された形」の係り先
- 原文: "which is presented in abbreviated form, in such a way that each author is represented as speaking in their own language"
- 現訳: 「言語名は省略された形で示され、それぞれの作者が…」
- 問題: 省略されているのは「議論（の内容）」であって言語名ではない。「（その議論は）要約された形で示され」とすべき。「言語名は」は原文にない。

### A-2. L93: indispensable の反転
- 原文: "But *k* is indispensable even in some Romance words: *kelki*, which I have just used, is an example"
- 現訳: 「しかし、k はいくつかのロマンス語の単語でも使えません。今使った単語もあります。」
- 問題: indispensable（不可欠）が「使えません」と正反対になっている。例語 *kelki* も訳から消えている。

### A-3. L99: found nowhere → 「不要」
- 原文: "the image for *qu* is more familiar than that of *k*, which in this case is in fact found nowhere"
- 現訳: 「qu のイメージは k のそれよりも親しみやすく、この場合、実はそれ自体が不要であることがわかります」
- 問題: 「（k の字形は）この場合実際にはどの言語にも見られない」の意。「不要」は誤り。なお同じ段落の「多数派に倒しました」も「多数派に従いました」が適切。

### A-4. L131: say a few words → 「単語を口述」
- 原文: "I ask that you say a few words as an introduction to the discussion on derivation"
- 現訳: 「派生に関する議論の導入として、いくつかの単語を口述するようお願いします」
- 問題: "say a few words" は「一言お話しください」の意の慣用句。「単語を口述する」は直訳による誤訳。

### A-5. L143: without the slightest grammatical coherence の反転
- 原文: "series of words of the same root and in a connected sense, but without the slightest grammatical coherence"
- 現訳: 「同じ語根でつながった意味の、文法的には最小限のまとまりのある一連の単語を見つけることができるのでしょうか」
- 問題: 「文法的な一貫性が全くない」が「最小限のまとまりのある」に反転。さらに原文は平叙文なのに「〜のでしょうか」と疑問文化している。

### A-6. L145: abolish and disallow → 「廃止したり許可する」
- 原文: "nor considered myself authorized to abolish and disallow some of them"
- 現訳: 「その一部を廃止したり許可する権限があると考えたわけでもありません」
- 問題: disallow（禁止する）が「許可する」と逆になっている。

### A-7. L146: 派生の方向の反転
- 原文: "a large number of verbs from which forms in *-entie* are derived"
- 現訳: 「多くの動詞は -entie の形から派生します」
- 問題: 「動詞から -entie 形が派生する」のであって逆ではない。

### A-8. L147: 文頭の文の意味破綻
- 原文: "This brings into the language either foreign forms or exceptional derivations."
- 現訳: 「外来形か例外的な派生形かは言語上重要です。」
- 問題: 「これは言語に外来形か例外的な派生形のいずれかを持ち込むことになる」の意。現訳は原文と無関係な文になっている。

### A-9. L167-168: O.J. の原則の段落が大きく欠落・破綻（最重要箇所の一つ）
- 原文: "Now my principle was: use for verbs the endings *-e, -i, -u*, where they were necessary because of derivatives, first in *-ione* and *-iv*: acte for *actione*, ... defini for *definitione, definitiv* ... But in other cases I preferred *-a* ... So I took *-a* in all cases where no known derived noun or adjective made another ending necessary or useful."
- 現訳: 「なぜなら、これらは派生語のために必要なものだからです。…というのも、派生する名詞や形容詞は他の語尾を必要としないし、使用することもないからです。」
- 問題:
  - 「私の原則はこうでした：派生語のために必要な場合には動詞語尾 -e, -i, -u を使う」という核心の宣言と、acte/actione, discuse/discusione, constitu/constitutione, defini/definitione といった例の列挙が丸ごと欠落。
  - 最終文は「既知の派生名詞・形容詞が他の語尾を必要としない場合はすべて -a を採用した」の意だが、現訳は「派生する名詞や形容詞は他の語尾を必要としない」と主張自体が変質している。
  - また L167 の「a Novialist wrote to me that it would be better if all verbs ended in *-a*」（あるノヴィアル使用者からの手紙の件）も訳抜け。

### A-10. L179: 例語が日本語に訳されてしまっている
- 原文: "(8) *-ion: action, construction, destination, expedition*"
- 現訳: 「(8) *-ion: 行動、建設、目的地、探検*」
- 問題: これらはオクツィデンタルの例語であり、原語のまま残すべき。意味として訳出してしまっている（しかも expedition を「探検」とするなど文脈にも合わない）。

### A-11. L191: Occidentalist → 「西洋人」
- 原文: "a conscientious Occidentalist"
- 現訳: 「良心的な西洋人」
- 問題: Occidentalist は「オクツィデンタル使用者（オクツィデンタリスト）」。「西洋人」は誤訳。L345 の「一部の西洋学者」（some Occidentalists）も同じ誤り。

### A-12. L197: line → 「ファイル」
- 原文: "what is the longeso of this very short line?"
- 現訳: 「この短いファイルの長さは何だろう？」
- 問題: line（線）が「ファイル」になっている。引用括弧も閉じていない。同段落では「Lat. *-tatem* から」の文も「Lat.の *tatem* から派生したものです。*-tatem*、Nも*-itate*を認めています」と断片化して破綻している。

### A-13. L204: this is the life → 「これは人生であり」
- 原文: "but this is the life and cannot be stopped by prohibitive rules"
- 現訳: 「これは人生であり、禁止規則で止めることはできない」
- 問題: 「これが言語の生きた姿（生命）であり」の意。「人生」は誤訳。

### A-14. L205, L207, L239: Ido → 「井戸」（系統的な取り違え）
- 原文: "as in Ido" / "this suffix, inherited from Ido" / "baleful heritages from Ido"
- 現訳: 「井戸のように」「井戸から受け継いだこの接尾辞」「井戸から受け継いだ禿げたような派生語」
- 問題: 言語名 Ido が「井戸」になっている（3箇所）。さらに L239 では baleful（有害な）が「禿げた」（bald との混同）になっている。

### A-15. L207: salient → 「妊娠」
- 原文: "using *e* as the less salient vowel ... is preferable and less shocking than the very salient vowels *a, o*"
- 現訳: 「妊娠しにくい母音として*e*を使うことは、妊娠した3つの母音*a, o*よりもショックが少なく好ましいと思うのですが、いかがでしょうか」
- 問題: salient（目立つ・際立った）が「妊娠」になっている（2箇所）。「3つの」も誤り（a, o の2つ）。「いかがでしょうか」は原文にない付け足し。

### A-16. L221: namely → 「ノミム」
- 原文: "Occidental here has a complicated system, namely:"
- 現訳: 「オクシデンタルは「ノミム」と呼ばれる複雑なシステムを持っている（この意味はよくわからないが）」
- 問題: 副詞 namely（すなわち）が固有名詞「ノミム」として音写され、訳者（機械）の注記「この意味はよくわからないが」まで本文に混入している。正しくは「すなわち次のような複雑な体系を持っています」。

### A-17. L228: 派生の方向の反転
- 原文: "*tyrannisar* from *tyrannic*"
- 現訳: 「*tyrannisar* から*tyrannic*」
- 問題: tyrannic から tyrannisar が作られる。方向が逆。

### A-18. L267: found nowhere → 「必要ない」、ほか
- 原文: "joining the auxiliary *ha* not with the perfect participle, but with the verbal theme ... This method is found nowhere."
- 現訳: 「助動詞*ha*を完了分詞に、しかし動詞のテーマで結合するという変わった方法をとっている。…この方法は必要ない。」
- 問題:
  - "not with A but with B"（完了分詞ではなく動詞語幹と結合）の構文が崩れている。
  - "found nowhere"（どの言語にも見られない）が「必要ない」になっている。
  - "in Occidental: *ha amat*" の Occidental が「オック語」になっている（オック語 = Occitan は別言語。L333 の「多くのオック語を避ける」も同様）。
  - "verbal theme" の「動詞のテーマ」は「動詞語幹」とすべき（L269 も同様）。

### A-19. L277: used only in this way → 「二通りしか使われない」
- 原文: "N with *tu*, which is used only in this way"
- 現訳: 「二通りしか使われない*tu*」
- 問題: 「この用法でしか使われない tu」の意。「二通り」は誤読。

### A-20. L293: 疑問文の取り違えと重複
- 原文: "How will you express in N the difference in the following sentence: ..."
- 現訳: 「次の文の違いは何だと思いますか。"Yo conosse le plu bon quam *tu*"と "yo conosse le plu bon quam *te*"の違いは何だと思いますか？」
- 問題: 「N ではこの違いをどう表現するのですか」が「違いは何だと思いますか」になっており、しかも同じ問いが二重に出力されている。続く "Even the possibility of inversion is such a convenient means that..." の文（「…の習得が、実用上の大きな利点に比例して立たないほど便利な手段なのだ」）も日本語として意味が取れない。

### A-21. L295, L321, L325: genitive → 「主格」（系統的な取り違え）
- 原文: "this genitive" / "I use this genitive only in very rare cases" / "If one were to use the genitive rarely"
- 現訳: 「この主格を完全に廃止する」「ごく稀にしかこの主格を使わない」「まれに主格を使うとしたら」
- 問題: genitive（属格・所有格）が一貫して「主格」（nominative）と誤訳されている（3箇所）。議論の対象は N の前置属格 *-n* であり、致命的な取り違え。

### A-22. L305, L313: accusative → 「非難語」（系統的な取り違え）
- 原文: "This accusative in my grammar was not mandatory" / "the need for such an accusative" / "using an accusative with the preposition *ye*"
- 現訳: 「このような非難語はespのように必須ではありませんでした」「このような非難語の必要性」「前置詞 *ye* を使って非難語を使う」
- 問題: accusative（対格）が「非難語」（accuse との混同）になっている（3箇所）。

### A-23. L292: 冒頭文の破綻
- 原文: "You say that a single form for the personal pronouns suffices"
- 現訳: 「代名詞の人称形があれば十分で」
- 問題: 「人称代名詞は単一の形で十分（＝格変化形は不要）だとあなたは言う」の意。「代名詞の人称形」では意味をなさない。

### A-24. L295: possessive pronouns → 「人称代名詞」
- 原文: "As for your possessive pronouns, one can still come to terms with the singular forms: *men, sen*, despite the fact that they do not fit well with the general Latin style..."
- 現訳: 「人称代名詞に関しては、単数形のままでも同意できる。」
- 問題: possessive（所有代名詞）が「人称代名詞」に。例語 *men, sen* と「ラテン的な基調に合わないにもかかわらず」の譲歩節が訳抜け。

### A-25. L321: 文の欠落による指示語の誤読誘発
- 原文: "your 'nor, vor, lor' is certainly shorter and therefore more convenient. But they are really artificially formed."
- 現訳: 「それはわかります。しかし、これらは本当に人為的に作られたものなのです。」
- 問題: 「あなたの nor, vor, lor は確かに短く便利だ」の一文が丸ごと欠落しており、その結果「これら」が直前の nusen 等を指すように誤読される（実際に人工的だと指摘されているのは相手の nor, vor, lor）。論旨が壊れる欠落。

### A-26. L297: nostri, vostri の比較の誤訳
- 原文: "How heavy would *nostri, vostri* be alongside *nor, vor*!"
- 現訳: 「nostri, vostri* は *nor, vor* と共にどれほど重いことだろう!」
- 問題: 「nor, vor に比べて nostri, vostri はどれほど重たいことか」の意。「と共に」は誤り。

### A-27. L333: attempted → 「証明した」
- 原文: "never before N attempted to this extent"
- 現訳: 「この程度ではN以前に誰もそれを証明したことはない」
- 問題: 「N 以前にここまで徹底して試みられたことはない」の意。「証明」「この程度では」とも誤り。

### A-28. L339: not entirely tenable のニュアンス
- 原文: "That they exist nowhere is not entirely tenable"
- 現訳: 「それらがどこにも存在しないというのは、まったくもって論外である」
- 問題: 原文は「完全には成り立たない（一概には言えない）」という穏当な反論。「まったくもって論外」は強すぎて語調が変わっている。同段落では「ヨーロッパの言語はこれまでそれなしでやってきたし、批判された形こそまさにそうした一般的な非性別語だ」の部分が訳抜け。また "Balto-Slavic" が「リトアニア・スラブ系言語」になっている（正しくは「バルト・スラヴ語派」）。

### A-29. L344: permit myself to mention → 「言及することを許可する」
- 原文: "I permit myself to mention the general negative Oc *ne*"
- 現訳: 「私は一般的な否定語 Oc *ne* に言及することを許可する」
- 問題: 「言及させていただきたい」の意。許可の主体が逆転している。同文中の「DESk, your *ne* は」には原文にない "your" が混入。

### A-30. L345: associated with → 「組み合わせることで」
- 原文: "one avoids misunderstandings and disadvantages associated with the prefix *in-*"
- 現訳: 「接頭辞 *in-* と組み合わせることで、誤解や不利益を回避することができます」
- 問題: 「接頭辞 in- に伴う誤解や不利益を回避できる」の意。「組み合わせることで」は反対方向の誤読。

### A-31. L353: the ranks of Oc → 「オークの仲間」
- 原文: "in the ranks of Oc there is still a group..."
- 現訳: 「オークの仲間には…グループがまだいるのです」
- 問題: Oc（オクツィデンタル陣営）が「オーク」になっている。

### A-32. L369: meeting → 「契約」、Mrs. の脱落
- 原文: "Mrs. Dave H. Morris (IALA), who through her generous subsidy has made possible the meeting"
- 現訳: 「寛大な助成金によってこの契約を可能にしてくださったDave H. Morris氏（IALA）」
- 問題: meeting（会合・会見）が「契約」に。また Mrs.（夫人）が「氏」になっている（デイヴ・H・モリス夫人。who has copied the report の「コピー」も当時の文脈では「筆写・清書」が適切）。

### A-33. L35: happy → 「幸せ」
- 原文: "a small word that we both accept and even consider very happy"
- 現訳: 「私たちが受け入れ、とても幸せだとさえ思う小さな言葉」
- 問題: ここでの happy は「(言葉・表現が)巧みな、うまくできた」の意。「非常にうまくできているとさえ考える」とすべき。

### A-34. L59: take firm root → 「確実な進出」
- 原文: "But to take firm root it must be not only easy to read..."
- 現訳: 「しかし、確実な進出のためには…」
- 問題: 「しっかりと根付くためには」の意。

### A-35. L117: 列挙の崩れ
- 原文: "Some are for the conservation of the historic image, some people even want to always have the sibilant sound, others want to write *k*..."
- 現訳: 「一つは歴史的イメージの保存のため、常に歯擦音であってほしいという人もいれば…」
- 問題: 「歴史的な字形の保存を支持する人もいれば」という人の列挙であり、「一つは…のため」では構文が壊れている。同段落の "regulated" の「規制される」も「決着がつく／整理される」が適切。

### A-36. L238: 反語の不明瞭化
- 原文: "Do these things not concern different methods of verbalization, but composition with prepositions."
- 現訳: 「これらのことは、言語化の異なる方法ではなく、前置詞を用いた構文に関係しているのだろうか。」
- 問題: 原文は「これらは動詞化の方法の違いではなく、前置詞（接頭辞）との合成の問題ではないか」という主張。現訳の「〜のだろうか」は疑念を表すように読め、論旨が曖昧になる。

---

## B. 訳抜け（文・節単位の欠落）

1. **L25**: "It is I who must thank you for your generous invitation"（感謝すべきは私の方です）が欠落。また "who demand modern naturalness..." は supporters に係る関係節だが、現訳では「補助言語」に係るように読める。
2. **L31**: "A very poor quality of the language is the system of endings"（語尾の体系はこの言語の非常に拙劣な点である）の導入文が欠落。
3. **L74**: "Learning another language perfectly requires enormous effort"（他の言語を完璧に習得するには多大な努力を要する）の主文が欠落し、「なぜなら」から始まる不完全な段落になっている。
4. **L76**: "and here I can make you, Mr. Wahl, the concession, that the importance is not the absolute number of people, but only the number of such cultured people who need communication with other nations"（重要なのは絶対数ではなく、他国との交流を必要とする教養層の数だ、というヴァール氏への譲歩）が丸ごと欠落。
5. **L167**: ノヴィアル使用者からの手紙の一文（A-9 参照）。
6. **L168**: O.J. の原則宣言と例の列挙（A-9 参照）。
7. **L205**: "The suffixes in Oc are therefore not as strictly mandatory as in other Interlingues, but are more explanatory and model-forming"（Oc の接尾辞は他の国際語ほど厳格に義務的ではなく、説明的・模範形成的なものだ）が欠落し、「なぜなら…」が前文と直結して論理が飛んでいる。
8. **L239**: "because *-is* does not mean to provide with something"（-is は「〜を備え付ける」の意味を持たないから）が欠落。
9. **L295**: "The same must be said about the pre-positive genitive in *n*."（n による前置属格についても同じことが言える）が欠落。直後の「そのようなもの」の指示対象が消えている。また *men, sen* と譲歩節の欠落（A-24 参照）。
10. **L321**: "your 'nor, vor, lor' is certainly shorter and therefore more convenient"（A-25 参照）。
11. **L339**: "until now the European languages have existed well without it, and the forms criticized in the end are just such common non-sexual words" が欠落（A-28 参照）。
12. **L277**: "even if that is heavier"（たとえ重くなるとしても）の譲歩が「重くなる」という単なる叙述に変化。

---

## C. 英語原文の未翻訳残存

- **L172**: 「-aの場合。… in -e.です。」 — "in -e" が未訳のまま残存し、句点と衝突。
- **L297**: 「と、F *nostre, notre*, in the parallel L *patre* S *padre* Prov *paire* F *père*, where even the *t* has disappeared; thus notre - nor in assimilation to them.における目に見える音声進化を通じて」 — 英文がほぼそのまま残存。なお原文（修正後）は "in assimilation to *lor*" であり "to them" は旧版の残骸と思われる。
- **L205**: 「*konfero* vice *conferentie*」 — "vice"（〜の代わりに）が未訳。
- **L231**: 「私たちは2つの接尾辞を持っています：ex.」 — "ex." が未訳。また主語 N が「私たち」に変わっている。
- **L332**: 「beyond *nule, nulo, nula, nul(i), omne, omno, omna, omni; te, to, ta, ti*, etc.となります」「and many others - all simple and easy and with universal use of endings that are international.これらはすべて…」 — 英文が残存し、後者は直後に日本語訳が重複している。
- **L339**: 「*alquó* = L *aliquod*, a little modernized.」 — "a little modernized" が未訳。

---

## D. 形式上の問題（Markdown・約物・重複）

1. **`*` の崩れ（多数）**: イタリック記号が片側だけ残る・単語の途中に入るなど。例: L172「*luce, perde... -。」、L176「(5) *-ie* (cp. 1): furie* (cp. 1): *furie*」、L295「*しかし、*nusen...」、L305「*プル・ボン・カム・ヴー」、L321「(Nusen*は」「n*は名詞にも」、L338「*su de illa "と言うでしょう」、L353「impossibil, irregulari, immobil* などの形については。」（文として不完全）。
2. **テキストの重複**: L175「(4) *-da*: (4) *-da*:」、L176（cp. 1 の重複）、L180「(9) …。(9)*-ore*…」、L181「irregular: 不定形：」、L293（疑問文の二重化）、L338「こう言うだろう。*su de illa "と言うでしょう。」
3. **矢印の混入**: L239「*natur→l-isar、americ→n-isar、vir→l-isar、regul→r-isar、possib→il-isar*」 — 単語内に「→」が混入し例語が壊れている。
4. **括弧・引用符の不対応**: L197「「この短いファイルの長さは何だろう？」（閉じ括弧なし）、L237「「講師が数学の問題を説明した。」（閉じ括弧なし）、L239「炭酸を作る、電気を作る」という意味から」（開き括弧なし）、L275・L277・L338 などの英語式引用符 `"..."` の混在。
5. **句読点の不統一**: L56-57 で「，」「．」（全角カンマ・ピリオド）が使われ、他は「、」「。」。L93 末尾「例: amike」、L109 末尾「chlor, clor.」など文末処理の不揃い。
6. **末尾のゴミ**: L178「- -。」、L175「-。」、L194「etc..。」など。

---

## E. 表記・用語の不統一

1. **言語名 Occidental の揺れ**: 「オクツィデンタル」（L7 ほか）／「オクシデンタル」（L221）／「オック語」（L267, L333 — 誤訳）／「オク」（L247, L338）／「オーク」（L353 — 誤訳）。冒頭の表記「オクツィデンタル」への統一が必要。
2. **例語のカタカナ化**: 原則として例語はラテン文字のままだが、一部でカタカナ化している。L243「*ステリル-イサ*：ステリル*」、L305「プル・ボン・カム・ヴー」「カム・ヴム」、L307「ヨハン・コノサ・マリア・プルボン・キャン・アンナ（ノム）」（直後の L308 はラテン文字のままで不揃い）、L309「ファ」、L239「ボタニサー」「クリチシーレン」、L345「インポッシビル、イレギュラー」。
3. **文体（です・ます／である）の混在**: 対話部分は基本です・ます調だが、L53、L171-181、L204-205、L237-239、L277、L293-297、L323-325、L358 などで である調・常体が混じる。同一話者の同一段落内でも切り替わる箇所がある（例: L197「行き着いた。…意味します」）。
4. **二人称・呼称の揺れ**: 「あなた」が基本だが、L99「先生ご自身も」、L275「君が来る前に」「教えてあげたいのです」と揺れており、L275 は語調も尊大に読める（原文は "I can please you ... by informing you" という丁寧な言い回し）。
5. **術語の揺れ**:
   - flexion: 見出し L249「語形変化」に対し L261「屈曲」、L265「屈折」。
   - verbal theme: 「動詞のテーマ」（L267, L269）→「動詞語幹」が適切。
   - "present theme" / "perfect theme": L172「主題現在」、L173「テーマ別完了」→「現在語幹」「完了語幹」が適切。
   - verbal substantive: L147「動詞の実体化」→「動詞名詞（の形成）」。
   - non-sexual forms: L332「非性別」、L338「ノンセクシュアルな形」で不統一（「性を区別しない形」などが無難）。
   - naturalistic school of interlinguistics: L30「自然主義的な言語学」→「国際語学（インターリングイスティクス）の自然主義学派」。
   - autonomous forms: L351「自治的形態」→「自律的な形」。

---

## F. 軽微な指摘

- **L7**: "The article" の「論文」→ 雑誌記事なので「記事」が適切（L93 の "article" は「論文」でも可だが「記事」で統一推奨）。
- **L21**: "the question of the best language" の「質問」→「問題」。
- **L49**: 「具体的な点を攻める前に」→「個別の論点に入る前に」。
- **L56**: "every civilized European" の「文明的なヨーロッパ人」→「教養ある（文明世界の）ヨーロッパ人」。
- **L89**: "(which is unusual)" の「これは異常」→「これは一般的でない／慣例に反する」。
- **L109**: "Note also *orkestre*" は良いが、L121 末尾の "Note also *gida*..." が「注意が必要です」になっている →「〜にも注目してください」の意。
- **L115**: 「N D wenn と wann において」→「N において D の wenn と wann を（区別すること）」と整理しないと略号が読み取れない。
- **L121**: 例語「g, go, gu」→ 原文は「ga, go, gu」。脱字。
- **L226**: 「(e) *perfect: perfectionar* から名詞を経て」→「perfect から名詞を経て perfectionar」の意で、語順が逆。
- **L142**: "verbal nouns" の「動名詞」→ 英文法の gerund と紛らわしいため「動詞由来の名詞（動詞名詞）」推奨。
- **L143**: "autonomous charades" の「自立した言葉遊び」→「（どの言語にも由来しない）独自の判じ物」のニュアンス。
- **L194**: 「特に有効です。これは…からです」の因果関係は原文にない（原文は e/a/o 語クラスの説明）。
- **L301-302（原文側）**: "plu bon can Anna" は原文の typo（cam）と思われる。訳注の検討対象。
- **L279/281（原文側）**: 脚注 "this preposition *tu* is necessary for the second person personal pronoun" は原文自体が不明瞭（tu が二人称代名詞と衝突するという E.W. の指摘か）。現訳は直訳だが、訳注があるとよい。

---

## 修正優先度の提案

1. **最優先**: セクション A の意味反転・取り違え（特に系統的なもの: genitive→主格、accusative→非難語、Ido→井戸、Occidentalist→西洋人、namely→ノミム、salient→妊娠）と、セクション B の訳抜け（特に A-9 / B-6 の O.J. の原則段落、A-25 / B-10 の論旨破壊）。
2. **高**: セクション C の未訳英文残存と、セクション D の重複・矢印混入・括弧不対応（読めば気づくレベルの破損）。
3. **中**: セクション E の表記・用語統一（特に Occidental の表記とカタカナ化例語の解消）。
4. **低**: セクション F の語調・訳語の磨き込み。

総じて、I・II は軽微な修正で済むが、III の L167 以降〜V は原文と突き合わせた再訳に近い作業が必要と思われる。
