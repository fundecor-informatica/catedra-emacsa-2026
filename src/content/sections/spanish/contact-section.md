---
enable: true
badge: "contacto"
title: "¿Tienes alguna pregunta o propuesta? <br /> Escríbenos."
description: "Estaremos encantados de ayudarte. Completa el formulario y nos pondremos en contacto contigo."
image: "/images/investigacion-home.avif"
imageAlt: "Contacto"
characterImage: "/images/character-3d.png"
characterImageAlt: "Personaje 3D"

form:
  emailSubject: "New contact form submission"
  submitButton:
    enable: true
    label: "Enviar Mensaje"
  inputs:
    - label: "Nombre Completo"
      placeholder: "Nombre Completo *"
      name: "Nombre Completo"
      required: true
      halfWidth: true
      defaultValue: ""
    - label: "Correo Electrónico"
      placeholder: "Correo Electrónico *"
      name: "Correo Electrónico"
      required: true
      type: "email"
      halfWidth: true
      defaultValue: ""
    - label: "Teléfono"
      placeholder: "Teléfono"
      name: "Teléfono"
      required: false
      type: "text"
      halfWidth: true
      defaultValue: ""
    - label: "Entidad / Empresa"
      placeholder: "Entidad / Empresa"
      name: "Empresa"
      required: false
      type: "text"
      halfWidth: true
      defaultValue: ""
    - label: "Asunto"
      placeholder: "Asunto *"
      name: "Asunto"
      required: true
      halfWidth: true
      dropdown:
        type: "select"
        items:
          - label: "Web Development"
            value: "Web Development"
            selected: false
          - label: "App Development"
            value: "App Development"
            selected: false
          - label: "UI/UX Design"
            value: "UI/UX Design"
            selected: false
          - label: "Other"
            value: "Other"
            selected: false
    - label: "Departamento Relacionado"
      placeholder: "Selecciona un departamento *"
      name: "Búsqueda Departamento"
      required: true
      halfWidth: true
      dropdown:
        type: "search"
        search:
          placeholder: "Buscar Departamentos..."
        items:
          - label: "Información General"
            value: "Información General"
            selected: false
          - label: "Actividades y Eventos"
            value: "Actividades y Eventos"
            selected: false
          - label: "Soporte Técnico"
            value: "Soporte Técnico"
            selected: false
          - label: "Colaboraciones"
            value: "Colaboraciones"
            selected: false
    - label: "Mensaje"
      tag: "textarea"
      placeholder: "Escribe tu mensaje *"
      name: "Mensaje"
      required: true
      halfWidth: false
      rows: "4"
      defaultValue: ""
    - label: "Búsqueda de Google"
      checked: false
      name: "Fuente de Usuario"
      required: true
      groupLabel: "¿Cómo nos has conocido?"
      group: "source"
      type: "radio"
      halfWidth: true
      defaultValue: ""
    - label: "Redes Sociales"
      name: "Fuente de Usuario"
      required: true
      group: "source"
      type: "radio"
      halfWidth: true
      defaultValue: ""
    - label: "Recomendación"
      name: "Fuente de Usuario"
      required: true
      group: "source"
      type: "radio"
      halfWidth: true
      defaultValue: ""
    - label: "Acepto los [Términos y Condiciones](/)"
      name: "Privacidad Acordada"
      value: "Aceptado"
      checked: false
      required: true
      type: "checkbox"
      halfWidth: false
      defaultValue: ""
    - note: success
      parentClass: "hidden text-sm message success"
      content: "¡Hemos recibido tu mensaje! Nos pondremos en contacto contigo lo antes posible."
    - note: deprecated
      parentClass: "hidden text-sm message error"
      content: "¡Algo salió mal! Por favor, inténtalo de nuevo."
---
