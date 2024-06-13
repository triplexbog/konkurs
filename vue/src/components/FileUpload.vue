<template>
  <div class="file-upload-container">
    <h2>Добавление файла</h2>
    <form @submit.prevent="uploadFile" class="file-upload-form">
      <div class="form-group">
        <label for="file" class="file-label">Выберите файл:</label>
        <input type="file" ref="fileInput" class="file-input" required>
      </div>
      <button type="submit" class="upload-button">Загрузить</button>
    </form>
  </div>
</template>

<script>
export default {
  methods: {
    uploadFile() {
      const file = this.$refs.fileInput.files[0];
      
      console.log('Файл:', file);
    }
  }
}
</script>

<style scoped>
.file-upload-container {
  text-align: center;
  margin-top: 20px;
}
.file-upload-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.form-group {
  margin-bottom: 15px;
}
.file-label {
  display: block;
  margin-bottom: 5px;
}
.file-input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 3px;
}

.upload-button {
  background-color: blue;
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}
</style>
