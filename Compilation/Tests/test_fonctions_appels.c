//hello

//les fonctions suivantes seront appelées dan la fonction main()
//Elles sont déclarées avant sinon elles seront inconnues dans main()

int multiplication(int a, int b){
	//corps de la fonction

	//le mot clé return renvoie une valeur à l'appelant.
	return a*b;
}

int addition(int a, int b){
	return a + b;
}

int soustraction(int a, int b){
	return a-b;
}

int my_pow(int a, int b){
	int a_temp;
	a_temp = a;
	while (b > 1){
		//On peut appeler un fonction dans le corps d'une autre fonction
		//et dans une boucle while par exemple
		a = multiplication(a,a_temp);
		b = soustraction(b,1);
	}
	return a;
}

int factorielle(int a){
	//on peut appeler une fonction dans une boucle for aussi
	int resultat;
	resultat = 1;
	for(a = a; a > 1; a = a - 1){
		resultat = multiplication(resultat,a);
	}
	return resultat;
}

int main(){
	int a;

	//on peut stocker le résultat d'une fonction dans une variable;
	a = multiplication(2,3);
	//resultat attendu : 6
	print(a);

	//Un paramètre de fonction peut être une variable ou une fonction.
	a = multiplication(a, addition(2,2));
	//resultat attendu : 24
	print(a);


	a = my_pow(2,3);
	//resultat attendu : 8
	print(a);

	//On peut faire des conditionnelles avec des résultats de fonction
	if(4 == addition(2,2)){
		print(4);
	}

	print(factorielle(5));//resultat attendu : 120
}
