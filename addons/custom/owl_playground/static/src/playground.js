/** @odoo-module **/

import { Component, useState, onMounted, useRef } from "@odoo/owl";
import {Counter} from './counter'
import {Todo} from './todo'

export class Playground extends Component {
    static components = { Counter, Todo }
    setup(){
        this.todos = useState([{id: 1, description: "Milk", done: true}, {id: 2, description: "Strawberry", done: false}])
        this.id= this.todos[this.todos.length-1].id

        const inputRef = useRef("inputRef")
        onMounted(() => {
            inputRef.el && inputRef.el.focus()
        })
    }

    toggleState(event,id){
      const todos = this.todos.map(todo => {
          if(todo.id === id) {
            todo.done = event.currentTarget.checked
      }
          return todo
      })
        this.todos = todos
    }

    addTodo(event){
        if(event.keyCode === 13 && event.currentTarget.value !== ""){
            this.todos.push(
                {
                    id: this.id +=1,
                    description: event.currentTarget.value,
                    done:false
                }
            )
            event.currentTarget.value = ""
        }
    }

    static template = "owl_playground.playground"
}
