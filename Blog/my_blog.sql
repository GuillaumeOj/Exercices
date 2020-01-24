-- Page principale
SELECT 'Page d\'accueil';
SELECT
    DATE_FORMAT(Article.date_publication, '%d/%m/%Y') AS date_publication,
    Utilisateur.pseudo AS auteur,
    Article.titre,
    Article.resume,
    COUNT(Commentaire.id) AS nombre_commentaires
FROM Article
JOIN Utilisateur ON Utilisateur.id = Article.auteur_id
JOIN Commentaire ON Commentaire.article_id = Article.id
GROUP BY Article.id
ORDER BY Article.date_publication DESC;

-- Page auteur
SELECT
    DATE_FORMAT(Article.date_publication, '%d %M \'%y') AS date_publication,
    Utilisateur.pseudo,
    Article.titre,
    Article.resume
FROM Article
JOIN Utilisateur ON Utilisateur.id = Article.auteur_id
WHERE Article.auteur_id = 2
ORDER BY Article.date_publication DESC;

-- Page catégorie
SELECT
    DATE_FORMAT(Article.date_publication, '%d/%m/%Y - %k:%i') AS date_publication,
    Utilisateur.pseudo,
    Article.titre,
    Article.resume
FROM Article
JOIN Utilisateur ON utilisateur.id = Article.auteur_id
JOIN Categorie_article ON Categorie_article.article_id = Article.id
WHERE Categorie_article.categorie_id = 3
ORDER BY Article.date_publication DESC;

-- Page de l'article
SELECT
    DATE_FORMAT(Article.date_publication, '%d %M \'%y à %k heures %i') AS date_publication,
    Article.titre AS titre_article,
    Article.contenu AS texte_article,
    Utilisateur.pseudo AS auteur_article,
    Categorie.nom AS nom_categorie
FROM Article
JOIN Utilisateur ON Utilisateur.id = Article.auteur_id
JOIN Categorie_article ON Categorie_article.article_id = Article.id
JOIN Categorie ON Categorie.id = Categorie_article.categorie_id
WHERE Article.id = 4;
-- Commentaires associés à l'article
SELECT 
    Commentaire.contenu AS commentaire,
    DATE_FORMAT(Commentaire.date_commentaire, '%d/%m/%Y') AS date_commentaire,
    Utilisateur.pseudo AS nom_auteur_commentaire
FROM Commentaire
JOIN Utilisateur ON Utilisateur.id = Commentaire.auteur_id
WHERE Commentaire.article_id = 2
ORDER BY Commentaire.date_commentaire;
