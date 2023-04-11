import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useCookies } from 'vue3-cookies'
import { extractUserFromSession } from '@/utils/session'

export const useMessaging = defineStore('messaging', () => {
  const contacts = ref()

  // Does not do anything by default, it is meant to be subscribed to by consumers
  function open(contact: any) { }

  return { contacts, open }
})
