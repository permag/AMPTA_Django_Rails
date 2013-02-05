class ApplicationController < ActionController::Base
  protect_from_forgery
 # helper_method :sidenav
  
  def sidenav
    @projects = Project.all
  end
end
