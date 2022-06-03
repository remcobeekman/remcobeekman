import { createRouter, createWebHistory } from "vue-router";
import Home from './components/HomePage'
import Create from './components/CreateSchieter'

const routes = [
    {
        path:'/',
        name:'home',
        component:Home
    },
     
    {
        path:'/create',
        name:'create',
        component:Create
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes,
})

export default router;