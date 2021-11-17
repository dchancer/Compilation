//hello

int main(){
	//declaration de variables
	int a;
	int b;
	int c;
	a = 5;

	//test boucle for fonctionnelle
	//resultat attendu : affichage de a 5 fois
	for(b = 0; b < a; b = b + 1){
		print(a);
	}
	//test boucle for avec erreur dans condition d'arrêt
	//resultat attendu : aucun affichage
	for(b = 0; b < -1; b = b + 1){
		print(a);
	}

	//test imbrication de boucle for
	//resultat attendu : affichage de 1 2 2 4
	for(b = 1; b < 3; b = b + 1){
		for(c = 1; c < 3; c = c + 1){
			print(b*c);
		}
	}

	//test boucle while
	//resultat attendu : affichage de 0 1 2 3 4
	c = 0;
	while(c < a){
		print(c);
		c = c + 1;
	}

	//test boucle while avec break
	//resultat attendu : aucun affichage mais pas de boucle infini car arret de la boucle
	c = 0;
	while(c < a){
		break;
		print(c);
	}

	//test boucle while avec continue
	//resultat attendu : aucun affichage car on saute le print(c)
	c = 0;
	while(c < a){
		c = c + 1; 
		continue;
		print(c);
	}

}
