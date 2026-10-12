# Static page bodies. {L:/path/} is replaced by a link to that path, {I:/wp-content/...} by an image src.
# {CTA} inserts the standard partner-referral box, {LATEST:n} the n latest articles.

CONTACT_EMAIL = "info@expatrimo.com"

PAGES = {}

PAGES['/'] = dict(
 title="Expatriation & Patrimoine",
 seo="Expatrimo, l'investissement pour les Français en Asie",
 desc="Expatrimo publie une information générale sur l'investissement immobilier et financier en France pour les Français expatriés en Asie.",
 body="""
<section class="hero">
  <div class="hero-img"><img src="{I:/wp-content/uploads/EXPATRIMO-CHINE-ASIE-BLOG.jpg}" alt="" loading="eager"></div>
  <div class="hero-text">
    <p class="kicker">Expatriés, comme vous. Depuis 2012.</p>
    <h1>L'investissement pour les Français en Asie</h1>
    <p class="lead">Immobilier en France, épargne, fiscalité des non-résidents, retraite, retour en France&nbsp;: Expatrimo décrypte l'actualité patrimoniale pour les Français qui vivent à Shanghai, Hong-Kong, Singapour, Séoul, Tokyo ou partout ailleurs en Asie.</p>
    <p class="actions"><a class="btn" href="{L:/actualites/}">Lire les articles</a> <a class="btn ghost" href="{L:/contact/}">Être mis en relation</a></p>
  </div>
</section>

<section class="wrap">
  <div class="section-head"><h2>À la une</h2><a href="{L:/actualites/}">Tous les articles →</a></div>
  {LATEST:6}
</section>

<section class="band">
  <div class="wrap">
    <div class="section-head"><h2>Nos thématiques</h2></div>
    <div class="cards three">
      <a class="theme" href="{L:/prestations/investissement-immobilier/}"><h3>Investissement immobilier</h3><p>Résidences services, EHPAD, nue-propriété temporaire, déficit foncier, SCPI&nbsp;: comprendre les formules adaptées à un investisseur qui vit loin de la France.</p><span>Découvrir →</span></a>
      <a class="theme" href="{L:/prestations/epargne-et-finance/}"><h3>Épargne et finance</h3><p>Assurance-vie, PER, produits structurés, liquidité&nbsp;: les grands principes pour faire fructifier son épargne pendant l'expatriation.</p><span>Découvrir →</span></a>
      <a class="theme" href="{L:/prestations/conseil-patrimonial/}"><h3>Stratégie patrimoniale</h3><p>Fiscalité des non-résidents, protection de la famille, retraite, transmission, retour en France&nbsp;: les questions à se poser à chaque étape.</p><span>Découvrir →</span></a>
    </div>
  </div>
</section>

<section class="wrap">
  <div class="section-head"><h2>Les grandes questions de l'expatrié</h2></div>
  <div class="cards">
    <div class="card-q"><h3>Se constituer une retraite complémentaire</h3><p>Expatrié, contrat local ou conjoint accompagnateur&nbsp;: préparer sa retraite est primordial lorsque l'on vit à l'étranger.</p><a href="{L:/actualites/faut-il-ouvrir-un-quand-travaille-en-asie/}">Lire&nbsp;: Faut-il ouvrir un PER quand on travaille en Asie&nbsp;?</a></div>
    <div class="card-q"><h3>Optimiser le patrimoine existant</h3><p>En Asie, votre situation financière et fiscale est différente de ce que vous connaissiez en France. L'expatriation est le bon moment pour faire le point.</p><a href="{L:/actualites/5-points-pour-mieux-gerer-ses-finances-lexpatriation-en-2024/}">Lire&nbsp;: 5 points pour mieux gérer ses finances à l'expatriation</a></div>
    <div class="card-q"><h3>Réduire ses impôts</h3><p>L'immobilier en France reste une valeur sûre, mais la taxation peut être importante. Des dispositifs existent pour investir en maîtrisant sa fiscalité.</p><a href="{L:/actualites/que-faire-en-2023-pour-baisser-ses-impots-sur-limmobilier-en-2024/}">Lire&nbsp;: Baisser ses impôts sur l'immobilier</a></div>
    <div class="card-q"><h3>Économiser et épargner</h3><p>Par son haut degré de sécurité et de protection du consommateur, l'assurance-vie française reste un cadre de référence pour l'épargne de précaution.</p><a href="{L:/actualites/avoir-une-assurance-vie-quand-est-expatrie/}">Lire&nbsp;: Avoir une assurance-vie quand on est expatrié</a></div>
    <div class="card-q"><h3>Protéger son conjoint et ses enfants</h3><p>La vie d'expatrié conduit souvent l'un des conjoints à mettre sa carrière entre parenthèses, et les études des enfants représentent une charge importante.</p><a href="{L:/actualites/expatriation-patrimoine-comment-proteger-sa-famille/}">Lire&nbsp;: Comment protéger sa famille</a></div>
    <div class="card-q"><h3>Préparer le retour en France</h3><p>Rapatrier ses fonds, anticiper l'achat d'une résidence principale, préparer un plan B&nbsp;: le retour se prépare pendant l'expatriation.</p><a href="{L:/actualites/preparer-son-plan-b/}">Lire&nbsp;: Préparer son plan B</a></div>
  </div>
</section>

{CTA}
""")

PAGES['/prestations/'] = dict(
 title="Nos thématiques",
 seo="Thématiques : immobilier, épargne et stratégie patrimoniale",
 desc="Les grandes thématiques d'Expatrimo pour les Français vivant en Asie : investissement immobilier, épargne et finance, stratégie patrimoniale.",
 body="""
<header class="page-head wrap"><h1>Nos thématiques</h1>
<p class="lead">Vous vivez à Hong-Kong, Shanghai, Singapour, Tokyo, Kuala Lumpur, Séoul ou ailleurs en Asie et vous vous demandez comment&nbsp;:</p></header>
<div class="wrap prose">
<ul class="checks">
<li>Préparer votre retraite</li><li>Faire fructifier votre épargne</li><li>Optimiser la fiscalité de vos revenus immobiliers</li><li>Préparer la transmission et la donation</li><li>Préfinancer les études de vos enfants</li><li>Préparer un retour en France</li>
</ul>
<p>Expatrimo publie une information générale et indépendante sur ces sujets. Nos articles sont organisés autour de trois grandes thématiques.</p>
</div>
<div class="wrap cards three">
  <a class="theme" href="{L:/prestations/conseil-patrimonial/}"><h3>Stratégie patrimoniale</h3><p>Le bilan patrimonial, la fiscalité, les grandes étapes&nbsp;: retour en France, départ à la retraite, transmission.</p><span>Découvrir →</span></a>
  <a class="theme" href="{L:/prestations/epargne-et-finance/}"><h3>Épargne et finance</h3><p>Placer son épargne, protéger son conjoint ou ses enfants, garder le contrôle de son capital.</p><span>Découvrir →</span></a>
  <a class="theme" href="{L:/prestations/investissement-immobilier/}"><h3>Investissement immobilier</h3><p>Revenus complémentaires, immobilier sans gestion, plus-value, fiscalité&nbsp;: les formules adaptées aux expatriés.</p><span>Découvrir →</span></a>
</div>
<div class="wrap prose">
<h2>Un regard d'expatriés</h2>
<ul>
<li>Une connaissance des défis propres à l'expatriation</li>
<li>Une compréhension des Français en Asie&nbsp;: familles multiculturelles, entrepreneuriat local, complexité des flux financiers</li>
<li>Une information générale, sans produit à vendre</li>
</ul>
<h2>Et si j'ai besoin d'un conseil personnalisé&nbsp;?</h2>
<p>Expatrimo ne fournit pas de conseil en investissement personnalisé et ne commercialise aucun produit. Si vous souhaitez aller plus loin, nous pouvons vous orienter vers un partenaire, basé en France ou à l'étranger, habilité à vous conseiller et à mettre en place des solutions adaptées à votre situation.</p>
</div>
{CTA}
""")

PAGES['/prestations/epargne-et-finance/'] = dict(
 title="Épargne et Finance",
 seo="Épargne et finance pour les Français expatriés en Asie",
 desc="Assurance-vie, PER : les grands principes de l'épargne pour les Français expatriés en Asie.",
 body="""
<header class="page-head wrap"><p class="kicker">Thématique</p><h1>Épargne et Finance</h1>
<p class="lead">Profiter de l'expatriation pour épargner et faire fructifier son capital.</p></header>
<div class="wrap split">
<div class="prose">
<p>Vous êtes Français en Asie et vous souhaitez&nbsp;:</p>
<ul class="checks"><li>Placer votre épargne de façon adaptée à votre situation</li><li>Protéger votre conjoint ou vos enfants</li><li>Préparer votre retraite</li><li>Créer du revenu complémentaire</li><li>Garder l'accès à votre capital</li><li>Épargner pour un futur projet</li><li>Financer les études supérieures de vos enfants</li></ul>
</div>
<figure><img src="{I:/wp-content/uploads/Investissement-financier-souscrire-assurance-vie-francaise-en-expatriation-EXAPTRIMO.jpg}" alt="Épargne et assurance-vie en expatriation" loading="lazy"></figure>
</div>
<div class="wrap prose">
<p>Il existe différentes formes d'investissement selon les objectifs, l'horizon de placement et la tolérance au risque de chacun. Voici les deux principales enveloppes utilisées par les Français de l'étranger.</p>
<h2>L'assurance-vie</h2>
<p>Il semble souvent difficile pour un Français résident à l'étranger de souscrire une assurance-vie française. C'est pourtant possible et légal&nbsp;: certaines compagnies d'assurance proposent des contrats adaptés aux non-résidents.</p>
<p>L'assurance-vie, placement préféré des Français, est un outil d'épargne à moyen et long terme. Elle permet de mettre de l'argent de côté pour un projet immobilier ou un complément de revenu. Les versements peuvent être uniques, ponctuels et&nbsp;/ ou réguliers.</p>
<p>L'assurance-vie française est aussi un outil de transmission, permettant de transmettre un capital dans un cadre fiscal favorable à toute personne que l'on désigne. C'est ainsi un moyen de prévoir sa succession ou de protéger un être cher. Contrairement à un placement offshore, une assurance-vie française peut être conservée au retour en France.</p>
<p>L'assurance-vie est avant tout une enveloppe fiscale, qui peut contenir divers investissements&nbsp;: actions européennes, américaines ou de pays émergents, obligations, fonds immobiliers, produits structurés ou Private Equity. Le choix des supports dépend de l'horizon de placement, de l'espérance de rendement et du niveau de risque accepté.</p>
<p>À lire&nbsp;: <a href="{L:/actualites/quest-ce-quune-assurance-vie/}">Qu'est-ce qu'une assurance-vie&nbsp;?</a> · <a href="{L:/actualites/avoir-une-assurance-vie-quand-est-expatrie/}">Avoir une assurance-vie quand on est expatrié</a></p>
<h2>Le PER</h2>
<p>Lancé en octobre 2019, le Plan d'Épargne Retraite est une solution d'épargne à long terme dédiée à la retraite par capitalisation. Plus souple que les systèmes précédents, il permet une sortie à la retraite en rente ou en capital (ou un mix des deux). Il permet de réduire ses impôts grâce aux sommes investies pour sa retraite, ce qui le rend particulièrement intéressant pour un retour en France. Il permet aussi de regrouper sous une même enveloppe les anciens plans de retraite d'entreprise.</p>
<p>Le PER peut être intéressant pour&nbsp;:</p>
<ul><li>Reprendre le contrôle de son investissement retraite</li><li>Réunir différents plans de retraite en un seul et même endroit</li><li>Défiscaliser des revenus perçus en France</li><li>Profiter de conditions de sortie souples</li></ul>
<p>À lire&nbsp;: <a href="{L:/actualites/faut-il-ouvrir-un-quand-travaille-en-asie/}">Faut-il ouvrir un PER quand on travaille en Asie&nbsp;?</a> · <a href="{L:/actualites/recuperer-votre-epargne-retraite-dentreprise/}">Récupérez votre épargne retraite d'entreprise&nbsp;!</a></p>
</div>
{CTA}
<section class="wrap"><div class="section-head"><h2>Articles Épargne &amp; Finance</h2><a href="{L:/actualites/}?cat=epargne-finance">Voir tout →</a></div>{CAT:Épargne & Finance:3}</section>
""")

PAGES['/prestations/conseil-patrimonial/'] = dict(
 title="Stratégie patrimoniale",
 seo="Stratégie patrimoniale et bilan pour les expatriés",
 desc="Pourquoi et comment faire le point sur son patrimoine pendant l'expatriation : bilan patrimonial, fiscalité, retraite, transmission, retour en France.",
 body="""
<header class="page-head wrap"><p class="kicker">Thématique</p><h1>Stratégie patrimoniale</h1>
<p class="lead">Faire le point sur sa situation financière pour définir une stratégie qui vous ressemble.</p></header>
<div class="wrap split">
<div class="prose">
<p>Les changements de situation dus à l'expatriation, aux évolutions familiales, au retour en France ou au départ à la retraite imposent souvent une redéfinition des plans d'investissement. Un bilan patrimonial complet fournit une photographie précise de sa situation financière actuelle et permet de prendre des décisions éclairées.</p>
<p>Un bilan patrimonial permet notamment de&nbsp;:</p>
<ul class="checks"><li>Avoir une vision complète de sa situation patrimoniale</li><li>Définir sa stratégie d'investissement</li><li>Optimiser sa fiscalité</li><li>Préparer son retour en France</li><li>Financer sa retraite</li><li>Organiser la transmission de son patrimoine</li></ul>
</div>
<figure><img src="{I:/wp-content/uploads/Conseil-Patrimonial-francais-expatrie-en-Asie-EXAPTRIMO.jpg}" alt="Stratégie patrimoniale pour les Français en Asie" loading="lazy"></figure>
</div>
<div class="wrap prose">
<h2>Les étapes d'un bilan patrimonial</h2>
<ol class="steps">
<li><strong>Évaluation initiale.</strong> Faire le point sur sa situation professionnelle d'expatrié, celle de son conjoint et son régime matrimonial, sa situation financière, ses placements financiers ou immobiliers et sa situation fiscale. Clarifier ses projets familiaux, ses projets de vie et ses envies de retour en France pour fixer des objectifs à court, moyen et long terme.</li>
<li><strong>Collecte d'informations.</strong> Rassembler tous les documents nécessaires pour une analyse complète de la situation.</li>
<li><strong>Analyse et stratégie.</strong> Analyser l'ensemble des actifs et passifs pour évaluer son patrimoine et élaborer une stratégie sur mesure.</li>
<li><strong>Recommandations.</strong> Traduire la stratégie en recommandations claires&nbsp;: investissements financiers et immobiliers, allègement de la fiscalité, transmission.</li>
</ol>
<h2>Pourquoi le faire pendant l'expatriation&nbsp;?</h2>
<p><strong>Une vision globale.</strong> Une compréhension complète de sa situation financière pour prendre des décisions éclairées.</p>
<p><strong>Des règles spécifiques.</strong> Le statut de non-résident modifie la fiscalité, l'accès au crédit et aux placements&nbsp;: les solutions pertinentes en France ne le sont pas toujours en Asie.</p>
<p><strong>Anticiper.</strong> Il est préférable de ne pas attendre de revenir en France pour sécuriser son avenir financier et optimiser son patrimoine.</p>
<p class="note">Expatrimo ne réalise pas de bilan patrimonial. Pour une étude personnalisée, nous pouvons vous orienter vers un conseiller habilité, en France ou à l'étranger.</p>
</div>
{CTA}
<section class="wrap"><div class="section-head"><h2>À lire sur le même thème</h2><a href="{L:/actualites/}">Voir tout →</a></div>{LATEST:3}</section>
""")

PAGES['/prestations/investissement-immobilier/'] = dict(
 title="Investissement immobilier",
 seo="Investir dans l'immobilier en France depuis l'Asie",
 desc="Résidences services, EHPAD, déficit foncier, SCPI, location meublée, nue-propriété temporaire : les formules d'investissement immobilier adaptées aux expatriés.",
 body="""
<header class="page-head wrap"><p class="kicker">Thématique</p><h1>Investissement immobilier</h1>
<p class="lead">Investir dans l'immobilier en France pendant son expatriation.</p></header>
<div class="wrap split">
<div class="prose">
<p>Un investissement immobilier peut répondre à plusieurs objectifs&nbsp;:</p>
<ul class="checks"><li>Constituer des revenus complémentaires pérennes</li><li>Échapper aux aléas de la gestion locative</li><li>Faire de la plus-value immobilière</li><li>Investir en France en maîtrisant sa fiscalité</li></ul>
<p>À distance, les formules qui ne demandent pas d'implication dans la gestion sont souvent les plus adaptées. Voici les principales.</p>
</div>
<figure><img src="{I:/wp-content/uploads/qb22jea6w_0.jpg}" alt="Investissement immobilier en France" loading="lazy"></figure>
</div>
<div class="wrap cards three">
  <div class="card-q"><h3>Résidences étudiantes et seniors</h3><p>Acheter un appartement dans une résidence services pour étudiants ou seniors, percevoir des loyers sans se soucier de la gestion, avec un statut fiscal avantageux (LMNP).</p><a href="{L:/actualites/investir-dans-une-residence-etudiante-pourquoi/}">En savoir plus</a></div>
  <div class="card-q"><h3>EHPAD et établissements de santé</h3><p>Se positionner sur un marché à la demande croissante et pérenne, et participer à la réponse à un besoin sociétal, avec des loyers versés par un exploitant via un bail commercial.</p><a href="{L:/actualites/la-sante-un-excellent-secteur-dinvestissement/}">En savoir plus</a></div>
  <div class="card-q"><h3>Déficit foncier</h3><p>Acheter un bien à rénover dans une localisation premium, réduire la fiscalité de ses revenus fonciers et acquérir un bien aux performances énergétiques améliorées.</p><a href="{L:/actualites/le-deficit-foncier-reduction-dimpot-et-investissement/}">En savoir plus</a></div>
  <div class="card-q"><h3>SCPI</h3><p>Profiter de l'immobilier professionnel sans gestion locative, avec un montant d'investissement flexible, en direct ou via une assurance-vie ou un PER.</p><a href="{L:/actualites/bien-choisir-une-scpi/}">En savoir plus</a></div>
  <div class="card-q"><h3>Location meublée</h3><p>Constituer un revenu complémentaire, disposer d'un pied-à-terre en France et profiter d'un statut fiscal avantageux.</p><a href="{L:/actualites/gestion-locative-les-differentes-formules-possibles/}">En savoir plus</a></div>
  <div class="card-q"><h3>Nue-propriété temporaire</h3><p>Acheter un bien avec une décote de 30&nbsp;% à 50&nbsp;% correspondant à environ 15 ans de loyers prépayés, sans gestion ni fiscalité sur les loyers, avec un potentiel de plus-value.</p><a href="{L:/actualites/strategie-dinvestissement-pour-les-expatries-la-nue-propriete-temporaire-en-france/}">En savoir plus</a></div>
</div>
<div class="wrap prose">
<h2>Les points de vigilance</h2>
<p><strong>La sélection du projet.</strong> L'emplacement, la réputation et le savoir-faire des intervenants, la rentabilité et la cohérence du prix d'achat avec le marché sont les critères essentiels.</p>
<p><strong>Le financement.</strong> Obtenir un crédit en tant que non-résident demande de la préparation. À lire&nbsp;: <a href="{L:/actualites/non-resident-comment-faciliter-lobtention-dun-credit-immobilier/}">Non-résident&nbsp;: comment faciliter l'obtention d'un crédit immobilier</a>.</p>
</div>
{CTA}
<section class="wrap"><div class="section-head"><h2>Articles Immobilier</h2><a href="{L:/actualites/}?cat=immobilier">Voir tout →</a></div>{CAT:Immobilier:3}</section>
""")

PAGES['/contact/'] = dict(
 title="Être mis en relation",
 seo="Être mis en relation avec un partenaire",
 desc="Expatrimo ne fournit pas de conseil personnalisé mais peut vous orienter vers un partenaire en France ou à l'étranger.",
 body="""
<header class="page-head wrap"><h1>Être mis en relation avec un partenaire</h1>
<p class="lead">Expatrimo est un média d'information. Nous ne fournissons pas de conseil en investissement personnalisé, mais nous pouvons vous orienter vers un partenaire, basé en France ou à l'étranger, qui pourra vous conseiller et mettre en place des solutions adaptées à votre situation.</p></header>
<div class="wrap split">
<div class="prose">
<h2>Comment ça marche&nbsp;?</h2>
<ol class="steps">
<li><strong>Vous décrivez votre besoin</strong> en quelques lignes&nbsp;: pays de résidence, sujet (immobilier, épargne, retraite, fiscalité, retour en France…).</li>
<li><strong>Nous identifions un partenaire</strong> dont l'activité correspond à votre demande.</li>
<li><strong>Le partenaire vous contacte</strong> directement. C'est lui qui analyse votre situation, vous conseille et met en œuvre les solutions, sous sa propre responsabilité.</li>
</ol>
<p class="note">Expatrimo n'intervient pas dans la relation entre vous et le partenaire, ne collecte aucun fonds et ne commercialise aucun produit. Vous restez libre de donner suite ou non.</p>
</div>
<form class="contact" id="contact-form">
  <label>Nom<input name="nom" required autocomplete="name"></label>
  <label>Email<input name="email" type="email" required autocomplete="email"></label>
  <label>Pays de résidence<input name="pays" placeholder="Chine, Singapour, Hong-Kong…"></label>
  <label>Sujet<select name="sujet"><option>Investissement immobilier</option><option>Épargne et assurance-vie</option><option>Retraite / PER</option><option>Fiscalité</option><option>Retour en France</option><option>Autre</option></select></label>
  <label>Votre demande<textarea name="message" rows="5" required></textarea></label>
  <label class="consent"><input type="checkbox" required> J'accepte que ma demande soit transmise à un partenaire afin qu'il me recontacte.</label>
  <button class="btn" type="submit">Envoyer ma demande</button>
  <p class="small">Le formulaire ouvre votre messagerie. Vous pouvez aussi écrire directement à <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</form>
</div>
""")

PAGES['/a-propos/'] = dict(
 title="À propos",
 seo="À propos d'Expatrimo",
 desc="Expatrimo est un média d'information sur l'investissement pour les Français expatriés en Asie.",
 body="""
<header class="page-head wrap"><h1>À propos</h1>
<p class="lead">Créé en 2012, Expatrimo est un média d'information consacré à l'investissement et au patrimoine des Français qui vivent en Asie.</p></header>
<div class="wrap split">
<div class="prose">
<h2>Notre mission</h2>
<p>Rendre l'information sur l'investissement immobilier et financier en France accessible aux Français d'Asie. Que vous soyez expatriés à Shanghai, Hong-Kong, Singapour, Séoul ou partout ailleurs en Asie, nos articles vous aident à comprendre les solutions existantes, leurs avantages et leurs risques.</p>
<p>Créé en 2012, expatrimo.com publie depuis plus de dix ans des articles sur l'immobilier en France, l'épargne, la fiscalité des non-résidents, la retraite et la préparation du retour.</p>
</div>
<figure><img src="{I:/wp-content/uploads/Conseillers-en-gestion-de-patrimoine-pour-les-francais-en-Asie-EXPATRIMO-2048x1463.png}" alt="Carte de la France et de l'Asie" loading="lazy"></figure>
</div>
<div class="wrap prose">
<h2>Notre ligne éditoriale</h2>
<p><strong>Une information générale.</strong> Les contenus publiés sur Expatrimo ont un caractère général et pédagogique. Ils ne tiennent pas compte de la situation particulière de chaque lecteur et ne constituent ni un conseil en investissement, ni une recommandation personnalisée, ni une sollicitation.</p>
<p><strong>Le regard de l'expatrié.</strong> Les sujets sont choisis pour répondre aux questions concrètes des Français d'Asie&nbsp;: investir à distance, épargner en tant que non-résident, protéger sa famille, préparer le retour.</p>
<p><strong>Aucun produit à vendre.</strong> Expatrimo ne commercialise aucun produit financier ou immobilier et ne reçoit pas de fonds de ses lecteurs.</p>
<h2>Et pour aller plus loin&nbsp;?</h2>
<p>Chaque situation est unique. Lorsque vous avez besoin d'un conseil adapté à votre cas, nous pouvons vous orienter vers un partenaire, basé en France ou à l'étranger, habilité à vous conseiller et à mettre en œuvre des solutions d'investissement. Le partenaire intervient alors sous sa propre responsabilité.</p>
<h2>Une communauté en Asie</h2>
<p>Nos lecteurs vivent dans toutes les grandes villes d'Asie&nbsp;: Shanghai, Pékin, Wuhan, Shenzhen, Canton, Hong-Kong, Singapour, Séoul, Busan, Bangkok, Kuala Lumpur, Tokyo, Taipei, Hô-Chi-Minh-Ville, Phnom Penh, Jakarta, Bangalore, Delhi…</p>
</div>
<div class="wrap gallery">
<img src="{I:/wp-content/uploads/Investissement-immobilier-en-couple-investir-en-expatriation-EXPATRIMO-768x1114.jpg}" alt="" loading="lazy">
<img src="{I:/wp-content/uploads/Francais-a-Singapour-gestion-patrimoine-francais-Expatrimo-768x1114.jpg}" alt="" loading="lazy">
<img src="{I:/wp-content/uploads/Investissement-immobilier-en-France-depuis-lAsie-expatriation-et-patrimoine-expatrimo-768x1114.jpg}" alt="" loading="lazy">
<img src="{I:/wp-content/uploads/Investir-dans-le-sud-de-la-France-investissement-immobilier-depuis-lAsie-768x1114.jpg}" alt="" loading="lazy">
</div>
{CTA}
""")

PAGES['/projets/'] = dict(
 title="Projets immobiliers",
 seo="Projets immobiliers : les grands types d'investissement",
 desc="Les grands types de projets immobiliers en France adaptés aux expatriés : nue-propriété temporaire, établissements de santé, résidences étudiantes et seniors.",
 body="""
<header class="page-head wrap"><h1>Projets immobiliers</h1>
<p class="lead">Expatrimo ne commercialise pas de programmes immobiliers. Cette page présente les grands types de projets que l'on rencontre sur le marché français et les critères pour les analyser.</p></header>
<div class="wrap cards three">
  <div class="card-q"><p class="tag">Nue-propriété temporaire</p><h3>Grandes villes, Côte d'Azur, Grand Paris</h3><p>Nice, Aix-en-Provence, Montpellier, Lyon, Rennes, Paris et sa proche banlieue&nbsp;: la nue-propriété temporaire se développe dans les zones à forte demande, où la valeur du bien à terme est la clé.</p><a href="{L:/actualites/bien-choisir-une-nue-propriete-temporaire/}">Bien choisir une nue-propriété temporaire</a></div>
  <div class="card-q"><p class="tag">Établissement de santé</p><h3>EHPAD en région parisienne et en région</h3><p>Les EHPAD sont des maisons de retraite médicalisées. L'investissement y garantit un revenu sur le long terme tout en participant à la réponse à un besoin croissant.</p><a href="{L:/actualites/investir-dans-un-ehpad/}">Investir dans un EHPAD</a></div>
  <div class="card-q"><p class="tag">Résidence étudiante, seniors</p><h3>Résidences services</h3><p>Proximité des écoles et universités, desserte, qualité du gestionnaire&nbsp;: les critères qui font la qualité d'une résidence services.</p><a href="{L:/actualites/investir-dans-une-residence-etudiante-pourquoi/}">Investir dans une résidence étudiante</a></div>
</div>
<div class="wrap prose">
<h2>Comment analyser un projet&nbsp;?</h2>
<ul>
<li><strong>L'emplacement&nbsp;:</strong> dynamisme économique, transports existants et à venir, demande locative.</li>
<li><strong>Les intervenants&nbsp;:</strong> réputation, ancienneté et savoir-faire du promoteur et de l'exploitant.</li>
<li><strong>Le prix&nbsp;:</strong> cohérence avec les prix du marché local, avant et après décote ou avantage fiscal.</li>
<li><strong>La sortie&nbsp;:</strong> existence d'un marché de revente et conditions de revente.</li>
</ul>
<p>À lire&nbsp;: <a href="{L:/actualites/tout-savoir-sur-lachat-immobilier-neuf/}">Tout savoir sur l'achat immobilier neuf</a> · <a href="{L:/actualites/grand-paris-lheritage-des-jo-2024/}">Grand Paris&nbsp;: l'héritage des JO 2024</a></p>
</div>
{CTA}
""")

PAGES['/documents/'] = dict(
 title="Documents",
 seo="Documents et ressources",
 desc="Ressources et guides Expatrimo pour les Français expatriés en Asie.",
 body="""
<header class="page-head wrap"><h1>Documents</h1>
<p class="lead">Les guides et articles de référence pour démarrer.</p></header>
<div class="wrap prose">
<h2>Guides thématiques</h2>
<ul>
<li><a href="{L:/prestations/investissement-immobilier/}">Investissement immobilier</a></li>
<li><a href="{L:/prestations/epargne-et-finance/}">Épargne et finance</a></li>
<li><a href="{L:/prestations/conseil-patrimonial/}">Stratégie patrimoniale</a></li>
</ul>
<h2>Articles de référence</h2>
<ul>
<li><a href="{L:/actualites/faut-il-payer-des-impots-en-france/}">Faut-il payer des impôts en France&nbsp;?</a></li>
<li><a href="{L:/actualites/quest-ce-quune-assurance-vie/}">Qu'est-ce qu'une assurance-vie&nbsp;?</a></li>
<li><a href="{L:/actualites/declarer-ses-biens-immobiliers/}">Déclarer ses biens immobiliers</a></li>
<li><a href="{L:/actualites/vendre-un-bien-immobilier-en-france/}">Vendre un bien immobilier en France</a></li>
<li><a href="{L:/actualites/non-resident-comment-faciliter-lobtention-dun-credit-immobilier/}">Non-résident&nbsp;: comment faciliter l'obtention d'un crédit immobilier</a></li>
<li><a href="{L:/actualites/quest-ce-que-la-liquidite-dun-placement/}">Qu'est-ce que la liquidité d'un placement&nbsp;?</a></li>
</ul>
</div>
""")

PAGES['/expatrimo-en/'] = dict(
 lang='en',
 title="EXPATRIMO : Investing in French real estate",
 seo="Expatrimo: information on investing in France from Asia",
 desc="Expatrimo is a media outlet providing general information on investing in France for expatriates living in Asia.",
 body="""
<header class="page-head wrap"><h1>EXPATRIMO: Investing in French real estate</h1>
<p class="lead">Founded in 2012, Expatrimo is an independent media outlet providing general information about investing in France for expatriates living in Asia.</p></header>
<div class="wrap split">
<div class="prose">
<h2>What we cover</h2>
<ul class="checks"><li>Property investment in France</li><li>Building retirement income</li><li>Capital growth and long-term savings</li><li>Tax rules for non-residents</li></ul>
<p>Our articles are written in French and explain the main investment solutions available to non-residents: serviced residences, nursing homes, temporary bare ownership, life insurance, retirement plans.</p>
<h2>Need personal advice?</h2>
<p>Expatrimo does not provide personalised investment advice and does not sell any product. If you want to go further, we can refer you to a partner based in France or abroad who is authorised to advise you and implement investment solutions.</p>
<p><a class="btn" href="{L:/contact/}">Get in touch</a></p>
</div>
<figure><img src="{I:/wp-content/uploads/ztdxtng-ltg.jpg}" alt="" loading="lazy"></figure>
</div>
""")

PAGES['/expatrimo-cn/'] = dict(
 lang='zh-CN',
 title="EXPATRIMO：投资法国房地产",
 seo="Expatrimo：法国投资资讯",
 desc="Expatrimo 是面向亚洲法国侨民的投资资讯媒体。",
 body="""
<header class="page-head wrap"><h1>EXPATRIMO：投资法国房地产</h1>
<p class="lead">Expatrimo 创立于2012年，是一家独立的资讯媒体，为居住在亚洲的读者提供有关在法国投资的一般性信息。</p></header>
<div class="wrap split">
<div class="prose">
<h2>我们关注的主题</h2>
<ul class="checks"><li>法国房地产投资</li><li>托管出租项目与稳定收益</li><li>租金预付型住宅项目（临时虚有权）</li><li>非居民税务</li></ul>
<h2>需要个性化建议？</h2>
<p>Expatrimo 不提供个性化投资建议，也不销售任何产品。如有需要，我们可以为您介绍位于法国或海外、具备资质的合作伙伴，由其为您提供建议并实施投资方案。</p>
<p><a class="btn" href="{L:/contact/}">联系我们</a></p>
</div>
<figure><img src="{I:/wp-content/uploads/0xup7storeu.jpg}" alt="" loading="lazy"></figure>
</div>
""")

PAGES['/mentions-legales/'] = dict(
 title="Mentions légales",
 seo="Mentions légales et avertissement",
 desc="Mentions légales et avertissement du site expatrimo.com.",
 body="""
<header class="page-head wrap"><h1>Mentions légales</h1></header>
<div class="wrap prose">
<h2>Éditeur</h2>
<p>Le site est édité par expatrimo.com.</p>
<p>Contact&nbsp;: <a href="mailto:{EMAIL}">{EMAIL}</a></p>
<h2>Hébergement</h2>
<p>[À compléter&nbsp;: nom et adresse de l'hébergeur.]</p>
<h2>Avertissement</h2>
<p>Les informations publiées sur expatrimo.com ont un caractère exclusivement général et informatif. Elles ne tiennent pas compte de la situation personnelle, financière ou fiscale des lecteurs et ne constituent ni un conseil en investissement, ni un conseil juridique ou fiscal, ni une recommandation personnalisée, ni une offre ou une sollicitation d'achat ou de vente d'un produit financier ou immobilier.</p>
<p>Les articles reflètent la réglementation et le contexte de marché à leur date de publication et peuvent ne plus être à jour. Tout investissement comporte des risques, notamment de perte en capital&nbsp;; les performances passées ne préjugent pas des performances futures.</p>
<p>Expatrimo ne fournit pas de conseil personnalisé. Lorsque cela est demandé, Expatrimo peut orienter le lecteur vers un partenaire tiers, en France ou à l'étranger. Ce partenaire agit sous sa propre responsabilité et selon la réglementation qui lui est applicable&nbsp;; Expatrimo n'intervient pas dans la relation entre le lecteur et le partenaire.</p>
<h2>Données personnelles</h2>
<p>Les informations transmises via la page de mise en relation sont utilisées uniquement pour traiter votre demande et, avec votre accord, la transmettre à un partenaire. Vous pouvez demander l'accès, la rectification ou la suppression de vos données en écrivant à <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</div>
""")
