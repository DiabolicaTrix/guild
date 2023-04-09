import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useCookies } from 'vue3-cookies'
import { extractUserFromSession } from '@/utils/session'

export const useSessionStore = defineStore('session', () => {
  const session = ref()
  const { cookies } = useCookies()

  if (cookies.get('token')) {
    session.value = extractUserFromSession()
  }

  function setSession(newSession: any) {
    console.log('Setting session', newSession)
    session.value = newSession
  }

  function clearSession() {
    session.value = null
  }

  return { session, setSession, clearSession }
})
