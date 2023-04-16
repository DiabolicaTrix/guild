<template>
  <main>
    <div class="content wrapper">
      <h1>Discover</h1>
      <div class="filters">
        <div class="filter">
          <input type="text" placeholder="Search" v-model="filters.search">
        </div>
        <div class="filter">
          <h3>Themes</h3>
          <div class="themes">
            <div class="theme" v-for="theme in filters.themes">
              <input type="checkbox" :id="theme.name" v-model="theme.checked">
              <label :for="theme.name">{{ theme.name }}</label>
            </div>
          </div>
        </div>
        <div class="filter">
          <h3>
            Filtres
          </h3>
          <div class="themes">
            <div class="theme" v-for="filter in filters.filters">
              <input type="checkbox" id="Poste disponible" v-model="filter.checked">
              <label :for="filter.name">{{ filter.name }}</label>
            </div>
          </div>
        </div>
      </div>
      <div class="projects">
        <ProjectCard v-for="project in projects" :value="project"></ProjectCard>
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import ProjectCard from '@/components/ProjectCard.vue';
import { fetcher } from '@/utils/fetcher';
import { ref, watch } from 'vue';
import debounce from 'lodash.debounce';
import 'vue3-carousel/dist/carousel.css'

type Theme = {
  id: string,
  name: string,
  checked: boolean
}

type Filter = {
  key: string,
  name: string,
  checked: boolean
}

type Filters = {
  search: string,
  themes: Theme[],
  filters: Filter[],
}

const filters = ref<Filters>({
  search: "",
  themes: [],
  filters: [
    {
      key: "available-roles",
      name: "Poste disponible",
      checked: false
    }
  ]
})

fetcher(`http://localhost:5000/themes`)
  .then(response => response.json())
  .then(data => {
    filters.value.themes = data;
  })

const projects = ref()
fetcher(`http://localhost:5000/projects`)
  .then(response => response.json())
  .then(data => {
    projects.value = data;
  })

async function loadProjects() {
  const params = new URLSearchParams();
  params.append("search", filters.value.search);
  filters.value.themes.forEach(theme => {
    if (theme.checked) {
      params.append("themes", theme.id);
    }
  })
  filters.value.filters.forEach(filter => {
    if (filter.checked) {
      params.append("filters", filter.key);
    }
  })
  const response = await fetcher(`http://localhost:5000/projects?${params.toString()}`);
  const data = await response.json()
  console.log(data)
  projects.value = data;
}

watch(filters, debounce(() => {
  loadProjects();
}, 500), { deep: true })

</script>

<style scoped>
main {
  display: flex;
  justify-content: center;

  margin-top: 36px;
}

.content {
  width: 1000px;

  display: flex;
  flex-direction: column;
  gap: 16px;

  padding: 16px;
}

.projects {
  /* Grid with 3 elements per row and center to parent*/
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  justify-items: center;
  gap: 16px;

}

.filters {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.filter {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.themes {
  display: flex;
  gap: 16px;
}

.theme {
  display: flex;
  align-items: center;
  gap: 8px;
  white-space: nowrap;
}
</style>
