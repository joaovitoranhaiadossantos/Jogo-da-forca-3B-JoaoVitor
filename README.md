# Jogo-da-forca-3B-JoaoVitor


Este repositório contém a versão aprimorada do Jogo da Forca em Python. A estrutura original do código foi modificada para cumprir a missão de categorizar as palavras por temas, tornando o jogo mais dinâmico e inteligente.

## Alterações Realizadas

### Organização por Temas
A lista linear de palavras única foi substituída por um **dicionário em Python (`dict`)**. Essa estrutura permitiu mapear categorias específicas (chaves) para suas respectivas listas de palavras (valores).

Os temas implementados foram:
* **Tecnologia:** Palavras relacionadas a computação e desenvolvimento.
* **Escola:** Vocabulário do ambiente escolar.
* **Jogos:** Termos do universo dos games.
* **Filmes:** Elementos da indústria cinematográfica.

### Sorteio Aleatório Duplo
A função `escolher_palavra()` foi reformulada para:
1.  Selecionar aleatoriamente um dos temas disponíveis no dicionário.
2.  Selecionar uma palavra aleatória pertencente exclusivamente ao tema escolhido.
3.  Retornar tanto a **palavra** quanto o **tema** para o fluxo do jogo.

### Exibição de Dicas na Interface
Para melhorar a experiência do usuário (UX), o jogo agora exibe uma dica logo no início da partida, informando qual é o tema da palavra secreta