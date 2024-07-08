# design

### roadmap
tldr: make base game, then focus on one mechanic per update.

base game:  
- stars
  - generating resources (eco/inf/rare) (rare resources needs to be automatic at star gen.)
    - rare resources - just basic implementation (no penalty yet)
  - capturing
  - building ships
  - star politic system (attack/defend planet politic wise)
- fleet movement
  - movement (planned movement)
  - capturing
  - fighting
  - merge/divide/defend
- group/player
  - players in group
  - players able to spend group resources
  - players can send resources to other groups (trade)

then focused updates on:
- star managament
  - simple numeric upgrades like in Neptune
- focus tree
- trade and diplomacy (more effects, statuses, usage of infulance)
- technology
- combat


### abstract
focus on politics, roleplay and long term planning trough resource management.

players are grouped into "fractions/imperiums/guilds" that has a shared goal and role within the group (admiral, minister of diplomacy etc.) with estabilished lore, which is extended by choice of players.
Simple to undestand mechanics promotes and put pressure on politics and roleplay.
Main mechanic for progressing group goal is "focus tree" similar in HoI or other paradox games. Players choose pre-determined focus steps, towards longer goal. Each step gives group small bonus/boon/lore, progress them forward. (viz mechanics.) 
Players has to manage intergroup politics, as different players has different roles (and in later versions goals and motivations too) and intergalatic politics, from war to trade to galaxy wide issues.
Players want to control stars in their sphere of influence, potencionally take more from oponents but multiple groups can have compatible or opposing goals. 
Each player control only a part of group resouces (economy/influence points) creating pressure on coop. 


### resources
the key resources for players are:
 - industry/economy/prouction points
   - abstract of industrial oputput of the group
   - non-transferable trough the rounds - or with massive penalty - motivates to spend as much as possible
   - used for building, creating, producing
   - ship building, colonising, building infrastructure and upgrading buildings
 - political/influence/diplomatic points
   - abstract for political output of the group
   - used for making things move, politics (agreements, pressure), persuation
   - declaration of war, moving fleet, gathering intel
 - rare resouces
   - exists for trade mechanic
   - every star produce and consumes random assertion of "rare resouces"
 - planets/stars
   - main production unit
   - produce economy/influence points, rare resources, ships, buildings, infrastrucure
   - core of every imperium
 - ?items (for later versions)
   - group/player can obtain items that provide small boon/resources
   - tradable, works as a small chaos agent to not make everything purely deterministic
 - fleet
   - military power of group
   - used for taking up stars

 
 ### mechanics 
 - trade 
   - main resouces can be traded by players for whatever players agree on
   - rare resouces should exists as more of a "optimalisation game" that stimulates activity - noncritical goods for imperium. Names and description can be mostly random and none of them should be "critical" to gameplay
     - there should be more types of rare resources than half of the stars - no group should be able to control them all and is forced to trade with others
     - every star generates and consume different rare resources
     - if the star demand is not fulfilled, given star get small production penalty (max. 10%)
     - comulative sum of all stars penalties should be allways displayed to motivate players to get rid of them
 - politics
   - interaction between players/groups
   - tied to infuence points
   - war, peace, aliance, trade...
   - every political action should take at least one round to make other players able to react
   - (later version) different groups can "add" or "oppose" to everyone else political actions (with penalty) 
 - planetary politics (production of influence points)  
   - stars generate influence points trough political power of population
   - (similar to stellaris)
   - (later) more population = more influence points created (population size can be from one type of building)
   - star politics is percentage based, multiple groups can have political parties on any star and "siphon" influence points from someone else.
   - using infuence points to suppre/promote any party on star. (always cheap to "defend" your stars)
   - allows "overtake" over forgotten/abbadoned planets, allows for simple-yet-deep resource management on who and where pressure politically even in time of peace.
 - capturing/fighting
   - now - same as in neptune. higer number win, defender shoots first
   - (very later) - simple rock-paper-scissors ships to tie-in small bonus/lore/counterplays etc.
   - even later - endless space "card strategy" system, every fleet would have a "strategy" picked from available imperium list of strategies, making small changes to fleet behaviour that are very slow and hard to change 
     - things like "first strike - first round 30% more dmg , bunkerbuster - takes iniciative first againist def fleet, shield gating - if fleet would be destroyed last round, negate the damage once" etc. 
     - make the simple one first ofc.
     - tie in for roleplay/focus/tech 
 - focus tree
   - serves for politics, roleplay and long term planning for whole group
   - progress is mainly time-based, cannot be sped up by players
     - but focus steps can have "obstacles" that players needs to get to progress, stimulating trade(eg, slowing them)  
   - after finishing focus step, everyone in game is informed about said group progress
   - can range from casus beli, resource gain, making some choices cheaper (cheaper war declaration, diplomacy etc.) or just lore bits to motivate roleplay that still moves said group forward 
   - can unlock/open/progress goals for group
   - allows for snowball/catchup/burn-it-all options for every player/group
   - (much later) opens posibility for small focus tree for every player for truly deep and complex roleplay/politics
 - later - development/building (neptune)
   - now - simple "economy/politics/ship building" with numbered upgrades that gets exponecionally expensive
 - ?technology
   - (later versions) make a base default research tree
   - (later+ versions) modify default reseatch tree for every group for personalised focus and problem
   - make tech rush possible but expensive (aka. less return of investment the more you invest)
   - cost would be both economy/influence points to make it especially hard to rush 
   - (alternativly make it more abstract and slow as you buy "projects" with clear goal but uncertain results)
   - possible to reseach make tied to focus tree, make it more focused on "roleplay" 
  

### round
 - move all fleets
 - produce resources
 - consume resources
 - progress research + focus
 - (send info to all players)