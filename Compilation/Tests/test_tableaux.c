int main(){
	//Test des tableaux
	//Declaration avec malloc
	int tab;
	tab=malloc(4);
	//Attribution de valeurs
	int i;
	for(i=0;i<4;i=i+1){
		tab[i]=i-2;
	}
	//Recuperation de valeurs
	for(i=0;i<4;i=i+1){
		print(tab[i]);
	}
	//Mise a jour de valeurs
	for(i=0;i<4;i=i+1){
		tab[i]=tab[i]+2;
		print(tab[i]);
	}
	print(tab[0]);
	print(tab[0+2]);
	print(tab[4&&0]);

}
