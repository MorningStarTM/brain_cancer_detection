const dragger = document.getElementById('dragger');
const dragger_text = document.getElementById('dragger_text');
const browseFileBtn = document.getElementById('browseFileBtn');
const fileSelectorInput = document.getElementById('fileSelectorInput');

const browseFileHandler = () => {
    fileSelectorInput.click();
}

fileSelectorInput.addEventListener('change', function (e) {
    file = this.files[0]
    uploadFileHandler(file)
});

dragger.addEventListener('dragover', (e) => {
    e.preventDefault();
    dragger_text.textContent = "Release to upload";
});

dragger.addEventListener('dragleave', () => {
    dragger_text.textContent = "Drag and Drop the Image";
});

dragger.addEventListener('drop', (e) => {
    e.preventDefault();
    file = e.dataTransfer.files[0]
    uploadFileHandler(file)
});

const uploadFileHandler = (file) => {
    const validFileExtension = ['image/jpeg', 'image/jpg', 'image/png'];
    if (validFileExtension.includes(file.type)){
        const fileReader = new FileReader();

        fileReader.onload = () => {
            const fileURL = fileReader.result;
            const imageTag = `<img src=${fileURL} alt=""/>`
            dragger.innerHTML = imageTag;
        }
        fileReader.readAsDataURL(file);
    }

}