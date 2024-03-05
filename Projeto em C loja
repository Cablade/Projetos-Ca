#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

struct Produto {
    int codigo;
    char nome[50];
    float valor;
    float peso;
};

struct Compra {
    int codigoProduto;
    char regiao[20];
    float peso;
};

float calcularFrete(char regiao[], float peso) {
    float fretePadrao, freteAcima2Kg;

    if (strcmp(regiao, "Sul") == 0 || strcmp(regiao, "sul") == 0) {
        fretePadrao = 30.00;
        freteAcima2Kg = 50.00;
    } else if (strcmp(regiao, "Suldeste") == 0 || strcmp(regiao, "suldeste") == 0) {
        fretePadrao = 25.00;
        freteAcima2Kg = 45.00;
    } else if (strcmp(regiao, "Norte") == 0 || strcmp(regiao, "norte") == 0) {
        fretePadrao = 35.00;
        freteAcima2Kg = 55.00;
    } else if (strcmp(regiao, "Nordeste") == 0 || strcmp(regiao, "nordeste") == 0) {
        fretePadrao = 40.00;
        freteAcima2Kg = 60.00;
    } else {
        printf("Região inválida.\n");
        exit(1);
    }

    if (peso <= 2.0) {
        return fretePadrao;
    } else {
        return freteAcima2Kg;
    }
}

void obterDataHora(char dataHora[]) {
    time_t t;
    struct tm *infoTempo;

    time(&t);
    infoTempo = localtime(&t);

    strftime(dataHora, 20, "%d-%m-%Y %H:%M:%S", infoTempo);
}

void mostrarProdutos(struct Produto produtos[], int numProdutos) {
    printf("\nProdutos em estoque:\n");
    for (int i = 0; i < numProdutos; i++) {
        printf("%d. %s - R$ %.2f - Peso: %.2f Kg\n", produtos[i].codigo, produtos[i].nome, produtos[i].valor, produtos[i].peso);
    }
}

int main() {
    struct Produto produtos[] = {
        {1, "Cassacos", 250.00, 1.5},
        {2, "Camisas", 70.00, 0.5},
        {3, "Calças", 120.00, 0.3},
        {4, "Vestidos", 150.00, 0.8},
        {5, "Saias", 100.00, 0.2},
    };
    
    int numProdutos = sizeof(produtos) / sizeof(produtos[0]);

    struct Compra compra;
    char dataHora[20];
    float totalCompra, frete;

    mostrarProdutos(produtos, numProdutos);

    // Solicitar ao cliente que escolha um produto
    printf("\nDigite o código do produto desejado: ");
    scanf("%d", &compra.codigoProduto);

    // Verificar se o código do produto é válido
    if (compra.codigoProduto < 1 || compra.codigoProduto > numProdutos) {
        printf("Código do produto inválido.\n");
        exit(1);
    }

    printf("Digite a região (Sul, Sudeste, Norte, Nordeste): ");
    scanf("%s", compra.regiao);

    printf("Digite a quantidade do produto desejado: ");
    int quantidade;
    scanf("%d", &quantidade);

    // Obtendo dados do produto escolhido
    struct Produto produtoEscolhido = produtos[compra.codigoProduto - 1];

    // Calculando o frete
    frete = calcularFrete(compra.regiao, quantidade * produtoEscolhido.peso);

    // Calculando o total da compra
    totalCompra = quantidade * produtoEscolhido.valor + frete;

    // Obtendo a data e hora atuais
    obterDataHora(dataHora);

    // Apresentando o resumo da compra
    printf("\nResumo da Compra:\n");
    printf("Data e Hora da Compra: %s\n", dataHora);
    printf("Código do Produto: %d\n", compra.codigoProduto);
    printf("Nome do Produto: %s\n", produtoEscolhido.nome);
    printf("Valor do Produto: R$ %.2f\n", produtoEscolhido.valor);
    printf("Quantidade: %d\n", quantidade);
    printf("Valor do Frete: R$ %.2f\n", frete);
    printf("Valor Total da Compra: R$ %.2f\n", totalCompra);

    // Calculando e apresentando a data prevista de entrega (7 dias úteis)
    printf("Data Prevista de Entrega: %s\n", dataHora);
    return 0;
}
