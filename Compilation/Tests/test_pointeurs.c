int main(){
	//Test des pointeurs
	//Declaration avec malloc pour une ou plusieurs cases
	int a;
	a=malloc(1);
	int tab;
	tab=malloc(4);
	//Attribution de valeurs
	*a=3+4;
	int i;
	for(i=0;i<4;i=i+1){
		*(tab+i)=i-2;
	}
	//Recuperation de valeurs
	print(*a);
	for(i=0;i<4;i=i+1){
		print(*(tab+i));
	}
	//Mise a jour de valeurs
	*a=*a-3;
	print(*a);
	for(i=0;i<4;i=i+1){
		*(tab+i)=*(tab+i)+2;
		print(*(tab+i));
	}


}
