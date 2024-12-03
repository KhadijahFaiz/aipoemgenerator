<template>
  <div class="min-h-screen bg-gradient-to-r from-primary-100 via-secondary-100 to-primary-200 flex flex-col items-center justify-center p-4">
    <div class="bg-white bg-opacity-90 rounded-lg shadow-2xl p-8 max-w-xl w-full">
      <h1 class="text-4xl font-bold text-center text-gradient mb-6">
        Saved Poems
      </h1>
      <div v-if="poems.length === 0" class="empty-state">No poems saved yet.</div>
      <div v-else class="poem-list">
        <div v-for="(poem, index) in poems" :key="index" class="poem-item">
          <div v-if="editIndex === index">
            <textarea v-model="editedPoem" class="edit-textarea"></textarea>
            <button @click="saveEditedPoem(index)" class="save-btn bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded">Save</button>
            <button @click="cancelEdit" class="cancel-btn bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ml-2">Cancel</button>
          </div>
          <div v-else>
            <pre>{{ poem }}</pre>
            <button @click="editPoem(index, poem)" class="edit-btn bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">Edit</button>
            <button @click="deletePoem(index)" class="delete-btn bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded ml-2">Delete</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'

export default {
  name: 'PoemGallery',
  setup() {
    const poems = ref([])
    const editIndex = ref(null) // Track which poem is being edited
    const editedPoem = ref('') // Store the current edited poem

    // Load saved poems from localStorage when the component is mounted
    onMounted(() => {
      const savedPoems = JSON.parse(localStorage.getItem('savedPoems') || '[]')
      poems.value = savedPoems
    })

    // Function to delete a poem from the list
    const deletePoem = (index) => {
      poems.value.splice(index, 1)
      localStorage.setItem('savedPoems', JSON.stringify(poems.value))
    }

    // Function to edit a poem
    const editPoem = (index, poem) => {
      editIndex.value = index
      editedPoem.value = poem
    }

    // Function to save the edited poem
    const saveEditedPoem = (index) => {
      poems.value[index] = editedPoem.value
      localStorage.setItem('savedPoems', JSON.stringify(poems.value))
      editIndex.value = null // Exit edit mode
    }

    // Function to cancel editing
    const cancelEdit = () => {
      editIndex.value = null
    }

    return {
      poems,
      editIndex,
      editedPoem,
      deletePoem,
      editPoem,
      saveEditedPoem,
      cancelEdit
    }
  }
}
</script>

<style scoped>
.poem-gallery {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.title {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 2rem;
  text-align: center;
  font-weight: bold;
}

.empty-state {
  text-align: center;
  font-size: 1.2rem;
  color: #7f8c8d;
  margin-top: 2rem;
}

.poem-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
}

.poem-item {
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 1.5rem;
  transition: transform 0.3s ease;
}

.poem-item:hover {
  transform: translateY(-5px);
}

pre {
  white-space: pre-wrap;
  word-wrap: break-word;
  text-align: left;
  font-family: 'Georgia', serif;
  font-size: 1rem;
  line-height: 1.6;
  color: #34495e;
}

.edit-textarea {
  width: 100%;
  height: 100px;
  padding: 10px;
  border-radius: 8px;
  border: 1px solid #ccc;
  font-family: 'Georgia', serif;
}

.save-btn, .cancel-btn, .delete-btn, .edit-btn {
  margin-top: 1rem;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.save-btn, .edit-btn {
  background-color: #27ae60;
  color: white;
}

.save-btn:hover, .edit-btn:hover {
  background-color: #2ecc71;
}

.delete-btn {
  background-color: #e74c3c;
  color: white;
}

.delete-btn:hover {
  background-color: #c0392b;
}
</style>