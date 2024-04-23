
// Função para validar o formulário de upload de arquivo
function validarFormulario() {
    var fileInput = document.getElementById('file');
    var errorMessage = document.getElementById('error-message');

    // Verificar se o campo de arquivo está vazio
    if (fileInput.files.length === 0) {
        errorMessage.innerText = 'Por favor, selecione um arquivo para enviar.';
        return false;
    } else {
        errorMessage.innerText = ''; // Limpar mensagem de erro se houver
        return true;
    }
}

// Adicionar manipuladores de eventos quando o documento HTML estiver totalmente carregado
document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('upload-form');

    // Adicionar um ouvinte de evento para o envio do formulário
    form.addEventListener('submit', function(event) {
        if (!validarFormulario()) {
            event.preventDefault(); // Impedir o envio do formulário se a validação falhar
        }
    });
});
