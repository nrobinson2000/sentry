{
  'use strict'

  const { fetch, parseInt } = window

  const image = document.getElementsByTagName('img')[0]
  const fullscreenButton = document.getElementById('fullscreen-button')
  const lightColorPicker = document.getElementById('light-color-picker')
  const toggleLightButton = document.getElementById('toggle-light-button')

  const mobileUpButton = document.getElementById('mobile-up')
  const mobileLeftButton = document.getElementById('mobile-left')
  const mobileRightButton = document.getElementById('mobile-right')
  const mobileDownButton = document.getElementById('mobile-down')

  const imageOffsetLeft = image.offsetLeft
  const imageOffsetTop = image.offsetTop

  let moving = false

  function move (direction) {
    if (!moving) {
      moving = true

      fetch(`/api/move?direction=${direction}`, {
        method: 'POST'
      })
    }
  }

  function stop () {
    if (moving) {
      moving = false

      fetch('/api/stop', {
        method: 'POST'
      })
    }
  }

  function changeLightColor (r, g, b) {
    fetch(`/api/light-color?r=${r}&g=${g}&b=${b}`, {
      method: 'POST'
    })
  }

  function toggleLight () {
    fetch('/api/toggle-light', {
      method: 'POST'
    })
  }

  function fire () {
    fetch('/api/fire', {
      method: 'POST'
    })
  }

  function handlePress (x, y) {
    let xDirection
    let yDirection

    if (x > 310) {
      xDirection = 1
    } else if (x < 170) {
      xDirection = 0
    }

    if (y > 370) {
      yDirection = 1
    } else if (y < 270) {
      yDirection = 0
    }

    if (xDirection !== undefined) {
      move(['left', 'right'][xDirection])
    }

    if (yDirection !== undefined) {
      move(['up', 'down'][yDirection])
    }
  }

  fullscreenButton.addEventListener('click', () => {
    image.requestFullscreen()
  })

  lightColorPicker.addEventListener('change', () => {
    let color = lightColorPicker.value

    let r = parseInt(color.slice(1, 3), 16)
    let g = parseInt(color.slice(3, 5), 16)
    let b = parseInt(color.slice(5, 7), 16)

    changeLightColor(r, g, b)
  })

  toggleLightButton.addEventListener('click', () => {
    toggleLight()
  })

  const mobileTimeout = 500

  mobileUpButton.addEventListener('click', () => {
    move('up')
    setTimeout(stop, mobileTimeout)
  })

  mobileLeftButton.addEventListener('click', () => {
    move('left')
    setTimeout(stop, mobileTimeout)
  })

  mobileRightButton.addEventListener('click', () => {
    move('right')
    setTimeout(stop, mobileTimeout)
  })

   mobileDownButton.addEventListener('click', () => {
    move('down')
    setTimeout(stop, mobileTimeout)
  })

  image.addEventListener('touchstart', event => {
    event.preventDefault()
    event.stopPropagation()

    for (const touch of event.touches) {
      handlePress(touch.clientX - imageOffsetLeft, touch.clientY - imageOffsetTop)
    }
  })

  image.addEventListener('dragstart', event => {
    event.preventDefault()
  })

  image.addEventListener('touchmove', event => {
    event.preventDefault()
    event.stopPropagation()
  })

  image.addEventListener('touchend', event => {
    event.preventDefault()
    event.stopPropagation()

    stop()
  })

  image.addEventListener('touchcancel', event => {
    event.preventDefault()
    event.stopPropagation()

    stop()
  })

  image.addEventListener('mousedown', event => {
    handlePress(event.offsetX, event.offsetY)
  })

  image.addEventListener('mouseup', () => {
    stop()
  })

  image.addEventListener('contextmenu', event => {
    event.preventDefault()
    event.stopPropagation()

    fire()
  })

  window.addEventListener('keydown', event => {
    switch (event.key) {
      case 'ArrowLeft':
        move('left')

        break

      case 'ArrowRight':
        move('right')

        break

      case 'ArrowUp':
        move('up')

        break

      case 'ArrowDown':
        move('down')

	break

      case 'Enter':
        toggleLight()
    }
  })

  window.addEventListener('keyup', event => {
    if (['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown'].includes(event.key)) {
      stop()
    }
  })
}
