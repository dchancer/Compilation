int toto(int a){
	print(a);
}

int titi(int a, int b, int c){
	print(b);
}

int main(){
	
	//Test des atomes
	//		"(" E ")"															Forme 1
	// 	"-" E																	Forme 2
	//		"!" E																	Forme 3
	//		constante															Forme 4
	//		identifiant														Forme 5
	//		identifiant "("E "," E "," ... ")"		Forme 6
	//		"*" identifiant					Forme 7
	
	//Forme 1
	int a;
	int b;
	int c;
	b=5;
	c=3;
	a=(3+4);
	print(a);
	a=(54/6*(b-c));
	print(a);
	
	//Forme 2
	a=-2;
	print(a);
	a=-b;
	print(a);
	a=-b+5;
	print(a);
	
	//Forme 3
	a=!(b==5); //attendu : 0
	print(a);
	a= !(5<=2);
	print(a);
	
	//Forme 4
	a=b;
	print(a);
	c=b;
	print(c);
	//a=b=c; ne fonctionne pas car pas de la forme a=b
	
	//Forme 5
	int ajouter;
	ajouter =1;
	while(a!=10){
		a=a+1;
		print(a);
	}
	//int while; ne fonctionne pas car while est un mot clé
	//int for; ne fonctionne pas car for est un mot clé
	//int debug; ne fonctionne pas car debug est un mot clé
	
	//Forme 6
	toto(a);
	titi(b,a,c);
	//while(a,c,b); ne fonctionne pas car while est un mot clé
	
	//Forme 7
	int ptr;
	ptr=malloc(1);
	*ptr=5;
	print(*ptr);
	//*while; ne fonctionne fonctionne pas car while est un mot clé
	
}


