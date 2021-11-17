//hello

//addition est le nom de la fonction suivante, elle renvoit une variable de type int
//et possède 2 paramètres
int addition(int a, int b){
	return a + b;
}

//Le nom des fonctions est important, il les différencie (même principe que les varaibles)
int addition(int a, int b, int c){
	return a + b + c;
}

//Dans notre langage, le type de retour d'une fonction est obligatoirement "int"
//resultat attendu : erreur
//void test(){}

//int main(){} est déjà une définition de fonction avec aucun paramètre.
int main(){
	print(addition(2,3));
	//print(addition(2,3,2)); // erreur car même nom de fonction.



	//Dans notre langage, la définition de fonction impose de mettre le mot clé "int" avant le nom
	//mais ce n'est pas encore le type de retour obligatoire : cette fonction main ne renvoit rien
	//et elle fonctionne tout de même. Cela peut être une amélioration future.
	 
}
