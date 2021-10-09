document.getElementById("connexion").addEventListener("submit",function(e) {
    e.preventDefault();
    
    var erreur ;
    var email=document.getElementById("email");
    var mdp=document.getElementById("mdp");
        
    
        if(!mdp.value){
            erreur="Champ de mot de passe est vide";
        }
     
        if(!email.value){
            erreur="Champ d'Email est vide";
        }
        
        
        if (erreur) {
            e.preventDefault();
            document.getElementById("erreur").innerHTML= erreur ; 
            return false ;
        } else{
            alert('Connexion faite!!');
        }
    }) ;