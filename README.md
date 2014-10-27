sphinxcontrib-hydradoc
======================

[Sphinx](http://sphinx-doc.org/contents.html) est un système de génération de documentation très utilisé dans le monde python.

[Hydra](http://www.hydra-cg.com/) est un langage, basé sur JSON (et [JSON-LD](http://json-ld.org/), [W3C Recommendation](http://www.w3.org/TR/json-ld/)) pour décrire une API REST sous une forme exploitable par les machines. À titre d'exemple, cette [description Hydra](http://www.markus-lanthaler.com/hydra/api-demo/vocab) décrit un service de bug-tracking. Une démo exploitant cette description est également disponible ici: [demo](http://www.markus-lanthaler.com/hydra/console/?url=http://www.markus-lanthaler.com/hydra/api-demo/). Il est important de noter que la console utilisée dans cette démo est totalement générique, n'ayant aucune connaissance a priori sur le service auquel elle se connecte.

Dans la partie droite de la console apparaît une documentation lisible du service, générée à partir de la description Hydra. L'objectif de ce Spint est de développer un module Sphinx permettant de générer avec Sphinx le même type de documentation à partir d'une description Hydra.

TODO
----
- [ ] Si on prend un **fichier** Hydra en entrée, déterminer le path exact, l'utilisateur donne juste le nom du fichier
- [ ] Pouvoir mettre une **uri** vers la description Hydra
- [ ] Définir les options de la ou des directive(s)


Développement
-------------

Pour aider le développement de cette extension nous conseillons la lecture de ces 
documentation :

- http://sphinx-doc.org/extdev/
- http://sphinx-doc.org/extdev/tutorial.html
- http://sphinx-doc.org/extdev/appapi.html
