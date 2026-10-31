# Arquitetura do Projeto

---

## 1. Objetivo e Escopo

---

## 2. Modelo de Dados

O projeto utiliza três classes principais para representar os dados e a estrutura hierárquica das fórmulas: `ItemFormula`, `Node` e `ArvoreFormula`.

### 2.1. ItemFormula

Representa os dados de um item pertencente a uma fórmula de produto.

**Atributos:**

| Atributo | Descrição |
|---|---|
| `nome` | Nome do item. |
| `quantidade` | Quantidade necessária do item. |
| `preco` | Preço associado ao item. |

A classe também disponibiliza métodos para atualização da quantidade e do preço.

### 2.2. Node

Representa um nó da árvore e é responsável por manter as referências necessárias à estrutura hierárquica.

A classe utiliza tipagem genérica (`Node[T]`), permitindo armazenar diferentes tipos de valores em sua estrutura. No contexto deste projeto, o valor armazenado é um objeto `ItemFormula`.

**Atributos:**

| Atributo | Descrição |
|---|---|
| `value` | Objeto armazenado no nó. Neste projeto, representa um `ItemFormula`. |
| `node_id` | Identificador individual do nó. |
| `tree_id` | Identificador da árvore à qual o nó pertence. |
| `parent` | Referência ao nó pai. É `None` quando não existe pai. |
| `children` | Lista de referências aos nós filhos. |
| `depth` | Profundidade do nó na árvore. |

### 2.3. ArvoreFormula

Representa e administra a estrutura hierárquica dos itens de uma fórmula.

A classe mantém duas estruturas principais:

| Atributo | Descrição |
|---|---|
| `root` | Referência ao nó raiz da árvore. |
| `nodes` | Dicionário que registra os nós pertencentes à árvore, utilizando seus identificadores como chaves. |

O dicionário permite localizar nós diretamente por seus identificadores, enquanto as referências entre pai e filhos mantêm a organização hierárquica.

---

## 3. Estrutura Node e ArvoreFormula

### 3.1. Relacionamento entre os objetos

Cada instância de `ArvoreFormula` mantém uma referência para sua raiz e um registro dos nós que compõem sua estrutura.

Cada `Node` contém um valor, representado por um objeto `ItemFormula`, além das referências para seu pai e seus filhos.

Os relacionamentos são mantidos por referências aos próprios objetos `Node`, permitindo que diferentes partes da árvore acessem o mesmo nó sem a necessidade de criar cópias.

### 3.2. Identificação dos nós

Cada nó possui um atributo `node_id`, destinado à sua identificação individual.

Essa identificação é especialmente importante porque diferentes nós podem armazenar itens com o mesmo nome. Portanto, o nome do item não deve ser utilizado como identificador único.

O atributo `tree_id` permite associar um nó à árvore correspondente, possibilitando a identificação da estrutura à qual ele pertence.

### 3.3. Registro dos nós

A classe `ArvoreFormula` utiliza um dicionário para registrar os nós da árvore, associando cada identificador à respectiva instância de `Node`.

Essa abordagem permite realizar buscas por identificador sem precisar percorrer toda a estrutura hierárquica.

As operações de inserção, remoção e alteração devem preservar a consistência entre o registro de nós e os relacionamentos mantidos por cada objeto.

---

## 4. Persistência no banco de dados

---

## 5. Reconstrução da árvore

---

## 6. Contratos dos métodos

| Operação | Recebe | Responsabilidade | Retorna |
|---|---|---|---|
| `ArvoreFormula.inserir()` | Nó e, opcionalmente, pai | Inserir um nó e preservar a estrutura | Resultado da operação ou exceção |
| `ArvoreFormula.buscar_por_id()` | ID | Localizar um nó registrado | `Node` ou `None` |
| `ArvoreFormula.remover()` | Nó ou ID, conforme a API escolhida | Remover o nó e seus descendentes | Resultado da operação |
| `ArvoreFormula.alterar()` | Nó e novo valor | Atualizar o conteúdo sem alterar a hierarquia | Resultado da operação |
| `FormulaService.explosao()` | Identificação da fórmula ou árvore | Preparar a representação hierárquica da fórmula | Estrutura de dados para consumo |
| `FormulaService.implosao()` | Fórmula e dados necessários | Executar o cálculo definido para a implosão | Resultado calculado |

---

## 7. Responsabilidades dos Services e Controllers

---

## 8. Formato de saida da explosão


---

## 9. Fluxo de atualização dos dados

---

## 10. Regras de integridade e tratamento de erros

