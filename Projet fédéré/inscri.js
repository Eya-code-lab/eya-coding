document.getElementById("inscri").addEventListener("submit",function(e) {
    e.preventDefault();
    
    var erreur ;
    var email=document.getElementById("email");
    var nom=document.getElementById("nom");
    var mdp=document.getElementById("mdp");
    var Cmdp=document.getElementById("cmdp");
        
        if(!cmdp.value){
            erreur="Champ de confirmation est vide";
            
        }
        if(!mdp.value){
            erreur="Champ de mot de passe est vide";
        }
        if(!nom.value){
            erreur="Champ de nom de l'utilisateur est vide";
        }
        if(!email.value){
            erreur="Champ d'Email est vide";
        }
        if (mdp.value!=cmdp.value) {
            erreur="verfier confirmation de mot de passe"
        }
        
        if (erreur) {
            e.preventDefault();
            document.getElementById("erreur").innerHTML= erreur ; 
            return false ;
        } else{
            alert('Inscription faite!!');
        }

    
}) ;