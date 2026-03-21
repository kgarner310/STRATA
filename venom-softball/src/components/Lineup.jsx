import React, { useState, useEffect } from 'react'

export default function Lineup({ players }) {
  const [order, setOrder] = useState([])

  useEffect(() => {
    setOrder(prev => {
      const existing = prev.filter(p => players.includes(p))
      const newPlayers = players.filter(p => !prev.includes(p))
      return [...existing, ...newPlayers]
    })
  }, [players])

  function moveUp(index) {
    if (index === 0) return
    setOrder(prev => {
      const next = [...prev]
      ;[next[index - 1], next[index]] = [next[index], next[index - 1]]
      return next
    })
  }

  function moveDown(index) {
    if (index === order.length - 1) return
    setOrder(prev => {
      const next = [...prev]
      ;[next[index], next[index + 1]] = [next[index + 1], next[index]]
      return next
    })
  }

  if (order.length === 0) {
    return <p className="message">Add players to the roster to build a lineup.</p>
  }

  return (
    <div>
      <h2 className="section-title">Batting Order</h2>

      {order.map((name, i) => (
        <div key={name} className="lineup-item">
          <span className="lineup-number">{i + 1}</span>
          <span>{name}</span>
          <div className="lineup-controls">
            <button onClick={() => moveUp(i)} disabled={i === 0}>&#9650;</button>
            <button onClick={() => moveDown(i)} disabled={i === order.length - 1}>&#9660;</button>
          </div>
        </div>
      ))}
    </div>
  )
}
