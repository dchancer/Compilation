int toto(){
	return 4;
}

int main(){
	//Pour tester voir arbre (afficher_arbre dans compilateur.py
  	//Doit reconnaitre et creer les tokens de :
	//+,-,*,/,%,^
	//<,>,<=,>=,==,!=
	//&&, ||, !
	//(,),;
	//=, , (virgule)
	// // (debut de commentaire)
	//constantes entieres
	//identifiant
	// mots-cles : for, while, if, else, debug, return, break, continue
	//		int
	//{,},[,]
	//EOF
	
	int a;
	a=(2+4-2/2)*2;
	a=3%4;
	a=2^2;
	a=3>5;
	a=4<7;
	a=3>=8;
	a=8<=7;
	a=3==3;
	a=3!=4;
	//hello
	a=(3) && 1;
	a=(3) || 1;
	a=!0;
	int i;
	for(i=0;i<2;i=i+1){
		
		if(i<1){
			continue;
		}
		
		else{
			break;
		}
	}
	while(i<3){
		i=i+1;
	}
	int tab;
	tab=malloc(2);
	tab[1]=2;
	a=toto();

}
