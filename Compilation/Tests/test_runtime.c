int main(){
	//Test des fonctions du runtime
	
	//puissance
	int a;
	a=2^2^3; //Attendu : 256
	print(a);
	a=2^(2+2);//Attendu : 16
	print(a);
	
	//malloc
	int tab;
	tab=malloc(4);
	tab[0]=89;
	tab[3]=7;
	print(tab[0]);
	print(tab[2]); //Attendu : 0 (car pas initialise)
	//ne doit pas marcher, ou alors par chance -> pas des zones reservees, 
	//peuvent être surecrites
	//tab[4]=46;
	//print(tab[4]);
	//Ne fait qu'un return 0
	free(tab);
	
	//print : teste auparavant sur les autres
	print(4/2);
	print(3>=4);

	//scanf : doit fonctionner avec les nombres negatifs et 0
	a=scanf();
	print(a);
	tab[1]=scanf();
	print(tab[1]);
}
