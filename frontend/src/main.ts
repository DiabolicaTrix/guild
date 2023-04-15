import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import '../src/assets/main.css'

import SyncLoader from 'vue-spinner/src/SyncLoader.vue'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faCaretDown, faUser, faSignOutAlt, faCaretLeft, faMinus, faPlus, faPenToSquare, faCheck, faBell, faHouse, faCompass } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faCaretDown, faUser, faSignOutAlt, faCaretLeft, faMinus, faPlus, faPenToSquare, faCheck, faBell, faHouse, faCompass)

const app = createApp(App)

app.use(createPinia())
app.use(router)
app.component('sync-loader', SyncLoader);
app.component('font-awesome-icon', FontAwesomeIcon)


app.mount('#app')
