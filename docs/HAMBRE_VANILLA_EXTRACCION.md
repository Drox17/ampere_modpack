# Fuentes vanilla de agotamiento (1.20.1)

Extraído del bytecode con `javap`: cada llamada a `Player.causeFoodExhaustion(float)` o
`FoodData.addExhaustion(float)` con la constante que pasa.

| Clase | Método | Vía | Valor |
|---|---|---|---:|
| MobEffect | public void m_6742_(net.minecraft.world.entity.LivingEntity, | Player.causeFoodExhaustion (agotamiento del jugador) | 0.005 |
| Player | protected void m_6475_(net.minecraft.world.damagesource.Dama | Player.causeFoodExhaustion (agotamiento del jugador) | 0.0 |
| Player | public void m_5706_(net.minecraft.world.entity.Entity); | Player.causeFoodExhaustion (agotamiento del jugador) | 2.0 |
| Player | public void m_6135_(); | Player.causeFoodExhaustion (agotamiento del jugador) | - |
| Player | public void m_6135_(); | Player.causeFoodExhaustion (agotamiento del jugador) | - |
| Player | public void m_36378_(double, double, double); | Player.causeFoodExhaustion (agotamiento del jugador) | - |
| Player | public void m_36378_(double, double, double); | Player.causeFoodExhaustion (agotamiento del jugador) | - |
| Player | public void m_36378_(double, double, double); | Player.causeFoodExhaustion (agotamiento del jugador) | - |
| Player | public void m_36378_(double, double, double); | Player.causeFoodExhaustion (agotamiento del jugador) | - |
| Player | public void m_36378_(double, double, double); | Player.causeFoodExhaustion (agotamiento del jugador) | 0.0 |
| Player | public void m_36378_(double, double, double); | Player.causeFoodExhaustion (agotamiento del jugador) | 0.0 |
| Player | public void m_36399_(float); | FoodData.addExhaustion (agotamiento del sistema de comida) | - |
| FoodData | public void m_38710_(net.minecraft.world.entity.player.Playe | FoodData.addExhaustion (agotamiento del sistema de comida) | 6.0 |
| FoodData | public void m_38710_(net.minecraft.world.entity.player.Playe | FoodData.addExhaustion (agotamiento del sistema de comida) | 6.0 |
| Block | public void m_6240_(net.minecraft.world.level.Level, net.min | Player.causeFoodExhaustion (agotamiento del jugador) | - |

