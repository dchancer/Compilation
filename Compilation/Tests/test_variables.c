//hello

int main(){
	//déclaration et affectation de a avec une valeur constante.
	int a;
	a = 3;
	print(a);

	//déclaration et affectation de b avec une variable définie précedemment.
	int b;
	b = a;
	print(b);

	//déclaration et affectation de c avec une multiplication de constantes
	//puis avec une multiplication de variables.
	//La valeur de c est écrasé à chaque nouvelle affectation
	int c;
	c = (3*4);
	print(c);
	c = (a*b);
	print(c);

	//tous les opérateurs fonctionnent
	c = (a/b);print(c);
	c = (2^2);print(c);
	c = (a-b);print(c);
	c = (a+b);print(c);

	//les variables peuvent aussi être des pointeurs
	int ptr;
	ptr = malloc(1);
	*ptr = 2;print(ptr);



	//Une variable déclarée dans un bloc est accessible uniquement dans son bloc et dans les blocs inférieurs.
	//Elle n'est pas accessible dans un bloc supérieur.
	//bloc #0
	//print(test);//ne fonctionne pas car test n'est pas encore déclarée
	{//bloc #1
		int test;
		test = 41;
		{//bloc#2
			print(test);
			//fonctionne car bloc inférieur, cela affiche la valeur de test déclarée 
			//dans le bloc #1 car elle n'a pas été redéclarée dans le bloc #2;
		}
	}
	//bloc #0
	//print(test);//ne fonctionne pas car bloc supérieur

	//La déclaration de variable fonctionne si et seulement si son nom n'est pas déjà utilisé
	//dans son bloc.
	int test;//bloc #0
	test = 42;print(test);
	//int test;//ne fonctionne pas car variable déjà déclarée dans bloc #0
	{
		int test;//bloc #1
		test = 43;print(test);
		//test est ici déclaré dans un nouveau bloc. la déclaration va donc fonctionner.
		{
			int test;//idem car bloc #2
			test = 44;print(test);
		}
		print(test);
	}
	print(test);


}
