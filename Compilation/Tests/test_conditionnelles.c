//hello

int main(){
	int a;
	int b;
	a = 3;
	b = -1;

	//test conditionnelle simple
	if(a == 3){
		print(a);
	}

	//test conditionnelle avec "else"
	//resultat attendu : on rentre dans le else donc affichage de b = -1
	if(a == 4){
		print(a);
	}
	else{
		print(b);
	}

	//test conditionnelles imbriquées + else
	//resultat attendu : ok pour le premier if -> not ok pour le 2eme if
	//on entre dans le else imbriqué donc affichage de b = -1
	if(a == 3){
		if(b == 0){
			print(0);
		}
		else{
			print(b);
		}
	}


	//test conditionnelles avec !=, >, >=, <, <=, &&, ||
	//resultat attendu : affichage de a 3 fois
	//rappel : a = 3
	if(a != 2){
		if(a > 2){
			if (a < 4){
				if(a <= 3){
					if(a >= 3){
						//rappel : b = -1
						if(a == 3 && b == -1){
							if(a == 3 || b == -2){
								print(a);
							}

							//test : entrer dans 2 if consécutivement (2 if dans le même bloc)
							if(b == -2 || a == 3){
								//le || fonctionne
								print(a);
								if(a == 3 && b == 0){
									//ne doit pas rentrer ici car b == -1
									print(b);
								}
								else{
									//le && fonctionne
									print(a);
								}
							}
						}
					}
				}
			}
		}
	}



}
